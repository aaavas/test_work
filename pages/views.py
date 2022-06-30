from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import TemplateView, ListView
from pages.forms import OsauhinguAndmedForm
from pages.models import Osalus, OsauhinguAndmedModel
from django.db.models import Q


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
            Q(nimi__icontains=query)
            | Q(registrikood__icontains=query)
            | Q(osanikud__nimi__icontains=query)
            | Q(osanikud__kood__icontains=query)
        )


def form_page_view(request):
    context = {}
    osalusFormset = inlineformset_factory(
        OsauhinguAndmedModel,
        Osalus,
        fields=("person", "osaluse_suurus", "asutaja"),
        extra=1,
    )
    if request.method == "POST":
        form = OsauhinguAndmedForm(request.POST)
        formset = osalusFormset(request.POST)
        if form.is_valid() and formset.is_valid():
            sum_segments = 0
            for segment_form in formset:
                if segment_form.cleaned_data["osaluse_suurus"]:
                    cleaned_segment = segment_form.cleaned_data["osaluse_suurus"]
                    sum_segments += int(cleaned_segment)
            kapital = int(form.cleaned_data["kapital"])
            if kapital == sum_segments:
                ou_instance = form.save()
                osalused = formset.save(commit=False)
                for osalus in osalused:
                    osalus.company = ou_instance
                    osalus.save()
                return redirect("profile", registrikood=ou_instance.registrikood)
    form = OsauhinguAndmedForm()
    formset = osalusFormset()
    context["form"], context["formset"] = form, formset
    return render(request, "form.html", context)


def ou_profile_view(request, registrikood):
    context = {}
    osauhing = get_object_or_404(OsauhinguAndmedModel, registrikood=registrikood)
    osanikud = []
    for osanik in osauhing.osanikud.all():
        nimi = osanik.nimi
        kood = osanik.kood
        osalus = osanik.osalus_set.get(company=osauhing)
        osa_suurus = osalus.osaluse_suurus
        asutaja = "Asutaja" if osalus.asutaja else ""
        osanikud.append([nimi, kood, osa_suurus, asutaja])
    context["ou"] = osauhing
    context["osanikud"] = osanikud
    return render(request, "profile.html", context)
