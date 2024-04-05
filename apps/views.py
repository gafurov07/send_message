from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from apps.forms import CustomUserCreateModelForm
from apps.models import CustomUser


# Create your views here.
class RegisterPage(CreateView):
    template_name = 'index.html'
    queryset = CustomUser.objects.all()
    form_class = CustomUserCreateModelForm
    success_url = reverse_lazy('created')

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class CreatedUser(TemplateView):
    template_name = 'created.html'

