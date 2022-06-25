from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import TemplateView, ListView
from django.views.generic.base import RedirectView
from pages.forms import OsauhinguAndmedForm
from pages.models import OsauhinguAndmedModel
from django.db.models import Q
from django.views.decorators.http import require_http_methods


# Create your views here.
class HomePageView(ListView):
    model = OsauhinguAndmedModel
    template_name = "avaleht.html"


class AboutPageView(TemplateView):
    template_name = "about.html"


class SearchResultsView(ListView):
    model = OsauhinguAndmedModel
    template_name: str = "search.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        return OsauhinguAndmedModel.objects.filter(
            Q(nimi__icontains=query) | Q(registrikood__icontains=query)
        )


def form_page_view(request):
    context = {}
    form = OsauhinguAndmedForm(request.POST or None)
    if form.is_valid():
        # save the form data to model
        form.save()
        return redirect(reverse("home"))
    context["form"] = form
    return render(request, "form.html", context)


def ou_profile_view(request, registrikood):
    context = {}
    osauhing = get_object_or_404(OsauhinguAndmedModel, registrikood=registrikood)
    context["ou"] = osauhing
    return render(request, "profile.html", context)
