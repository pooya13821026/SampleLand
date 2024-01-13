from django.views.generic import CreateView
from .forms import ContactUsModelForm


class ContactUsView(CreateView):
    template_name = 'contact/contact_us.html'
    form_class = ContactUsModelForm
    success_url = '/contact-us/'

    # def get(self, request):
    #     contact_form = ContactUsModelForm()
    #     setting = SiteSetting.objects.filter(main_setting=True).first()
    #     context = {
    #         'form': contact_form,
    #         'setting': setting
    #     }
    #     return render(request, 'contact/contact_us.html', context)
    #
    # def post(self, request):
    #     contact_form = ContactUsModelForm(request.POST)
    #     if contact_form.is_valid():
    #         contact_form.save()
    #         return redirect(reverse('home_page'))
