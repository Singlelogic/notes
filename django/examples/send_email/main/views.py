from django.views.generic import CreateView

from .forms import ContactForm
from .models import Contact
from .service import send


class ContactView(CreateView):
    """Displaying the subscription form by email."""
    model = Contact
    form_class = ContactForm
    success_url = '/main'
    template_name = 'main/contact.html'

    def form_valid(self, form):
        form.save()
        send(form.instance.email)
        return super().form_valid(form)