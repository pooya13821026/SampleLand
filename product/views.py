from django.db.models import Count
from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from product.forms import SearchForm
from product.models import Product, ProductCategory, ProductBrand, ProductSeen, ProductGallery
from utilities.http_service import get_user_ip


class ProductListView(ListView):
    model = Product
    template_name = 'product/product_list.html'
    ordering = ['-create_date']
    paginate_by = 12

    def get_queryset(self):
        query = super(ProductListView, self).get_queryset()
        data = query.filter(is_active=True, is_delete=False)
        category_name = self.kwargs.get('cat')
        brand_name = self.kwargs.get('br')
        if brand_name is not None:
            query = query.filter(brand__url_title__iexact=brand_name)
            return query
        if category_name is not None:
            query = query.filter(category__url_title__iexact=category_name)
            return query
        return data


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product_details.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data()
        product = self.object
        user_ip = get_user_ip(self.request)
        user_id = None
        if self.request.user.is_authenticated:
            user_id = self.request.user.id
        viewed: bool = ProductSeen.objects.filter(viewer_ip__iexact=user_ip, product=product).exists()
        if not viewed:
            new_view = ProductSeen(
                viewer_ip=user_ip,
                user_id=user_id,
                product_id=product.id
            )
            new_view.save()
        my_product = kwargs.get('object')
        context['related_product'] = Product.objects.filter(brand_id=my_product.brand_id).all()[:8]
        galleries = list(ProductGallery.objects.filter(product_id=my_product.id).all()[:4])
        galleries.insert(0, my_product)
        context['product_galleries'] = galleries
        return context


def product_categories_component(request: HttpRequest):
    product_categories = ProductCategory.objects.annotate(product_count=Count('product_categories')).filter(
        is_active=True,
        is_delete=False)
    context = {
        'categories': product_categories
    }
    return render(request, 'product/components/product_categories_component.html', context)


def product_brands_component(request: HttpRequest):
    product_brands = ProductBrand.objects.annotate(brand_count=Count('product')).filter(
        is_active=True,
        is_delete=False)
    context = {
        'brands': product_brands
    }
    return render(request, 'product/components/product_brands_component.html', context)


def search(request):
    product = Product.objects.all()
    form = SearchForm()
    if 'search' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            cd = form.cleaned_data['search']
            product = product.filter(title__icontains=cd)
    return render(request, 'product/product_list.html', {'form': form, 'object_list': product})
