from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from pages.models import OsauhinguAndmed

# Create your views here.
class HomePageView(ListView):
    model = OsauhinguAndmed
    template_name = "avaleht.html"


class AboutPageView(TemplateView):
    template_name = "about.html"
