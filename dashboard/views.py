from django.contrib.auth import get_user, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView
from order.models import Order, OrderDetail
from .forms import EditProfileForm, ChangePasswordForm


@method_decorator(login_required, 'dispatch')
class Dashboard(TemplateView):
    template_name = 'dashboard/dashboard.html'


@method_decorator(login_required, 'dispatch')
class EditProfile(View):
    def get(self, request: HttpRequest):
        user = get_user(request)
        form = EditProfileForm(instance=user)
        context = {
            'form': form,
            'user': user
        }
        return render(request, 'dashboard/edit_profile.html', context)

    def post(self, request: HttpRequest):
        user = get_user(request)
        form = EditProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save(commit=True)
        context = {
            'form': form,
            'user': user
        }
        return render(request, 'dashboard/edit_profile.html', context)


@method_decorator(login_required, 'dispatch')
class ChangePass(View):
    def get(self, request: HttpRequest):
        change_pass_form = ChangePasswordForm()
        context = {
            'change_pass_form': change_pass_form,
        }
        return render(request, 'dashboard/change_pass.html', context)

    def post(self, request: HttpRequest):
        change_pass_form = ChangePasswordForm(request.POST)
        if change_pass_form.is_valid():
            user = get_user(request)
            if user.check_password(change_pass_form.cleaned_data.get('current_password')):
                user.set_password(change_pass_form.cleaned_data.get('new_password'))
                user.save()
                logout(request)
                return redirect(reverse('login_page'))
            else:
                change_pass_form.add_error('current_password', 'کلمه عبور وارد شده صحیح نیست')
        context = {
            'change_pass_form': change_pass_form,
        }
        return render(request, 'dashboard/change_pass.html', context)


@login_required
def user_dashboard_component(request):
    return render(request, 'dashboard/component/dashboard_component.html')


@login_required
def user_cart(request: HttpRequest):
    user_order, create = Order.objects.prefetch_related('orderdetail_set').get_or_create(is_order_paid=False,
                                                                                         user_id=request.user.id)
    total = user_order.total_price()
    context = {
        'order': user_order,
        'total': total
    }
    return render(request, 'dashboard/user_cart.html', context)


def delete_from_order_items(request: HttpRequest):
    item_id = request.GET.get('detail_id')
    if item_id is None:
        return JsonResponse({
            'status': 'item-id-not-found'
        })
    del_number , del_item = OrderDetail.objects.filter(id=item_id,order__is_order_paid=False,order__user_id=request.user.id).delete()

    if del_number == 0:
        return JsonResponse({
            'status': 'item-not-found'
        })
    user_order, create = Order.objects.prefetch_related('orderdetail_set').get_or_create(is_order_paid=False,
                                                                                         user_id=request.user.id)
    total = user_order.total_price()
    context = {
        'order': user_order,
        'total': total
    }
    html_component = render_to_string('dashboard/component/user_cart_component.html', context)
    return JsonResponse({
        'status': 'success',
        'data': html_component
    })
