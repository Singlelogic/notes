from django.views.generic import CreateView

from .forms import ContactForm
from .models import Contact
from .tasks import send_spam_email


class ContactView(CreateView):
    """Displaying the subscription form by email."""
    model = Contact
    form_class = ContactForm
    success_url = '/main'
    template_name = 'main/contact.html'

    def form_valid(self, form):
        form.save()
        send_spam_email.delay(form.instance.email)
        return super().form_valid(form)