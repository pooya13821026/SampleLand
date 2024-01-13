from django.db.models import Count
from django.shortcuts import render
from django.views.generic import TemplateView
from product.models import Product
from setting.models import FooterLinkTitle, SiteSetting, Slider


class HomeView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data()
        context['sliders'] = Slider.objects.filter(is_active=True)
        context['newest_products'] = Product.objects.filter(is_active=True, is_delete=False).order_by('-create_date')[
                                     :8]
        most_view_product = Product.objects.filter(is_active=True,is_delete=False).annotate(view_count=Count('productseen')).order_by('-view_count')[:12]
        context['most_view_product'] = most_view_product
        return context


def header_component(request):
    settings = SiteSetting.objects.filter(main_setting=True).first()
    context = {
        'settings': settings
    }
    return render(request, 'shared/header_component.html', context)


def footer_component(request):
    footer_link_titles = FooterLinkTitle.objects.all()
    for item in footer_link_titles:
        item.footerlink_set
    settings = SiteSetting.objects.filter(main_setting=True).first()
    context = {
        'footer_link_titles': footer_link_titles,
        'settings': settings
    }
    return render(request, 'shared/footer_component.html', context)
