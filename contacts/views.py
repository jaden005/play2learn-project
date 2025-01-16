import html
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from common.utils.email import send_email
from .forms import ContactForm

class ContactAppView(FormView):
    template_name = 'contacts/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contacts:thanks')

    def form_valid(self, form):
        data = form.cleaned_data
        to = 'jaden.neal142@gmail.com'
        subject = 'Contact From'
        content = f'''<p>Hey HR Manager!</p>
            <p>Email received:</p>
            <ol>'''
        for key, value in data.items():
            label = key.replace('_', ' ').title()
            entry = html.escape(str(value), quote=False)
            content += f'<li>{label}: {entry}</li>'
        
        content += '</ol>'

        send_email(to, subject, content)
        return super().form_valid(form)

class ContactAppThanksView(TemplateView):
    template_name = 'contacts/thanks.html'