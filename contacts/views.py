from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from .forms import ContactForm

class ContactAppView(FormView):
    template_name = 'contacts/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contacts:thanks')

class ContactAppThanksView(TemplateView):
    template_name = 'contacts/thanks.html'