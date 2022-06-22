from django.shortcuts import render

from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm

class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/bboard/"
    template_name = "register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)
