from django.urls import path
from .views import (
    form_page_view,
    HomePageView,
    AboutPageView,
    SearchResultsView,
    ou_profile_view,
)
from . import views


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("form/", form_page_view, name="form"),
    path("search/", SearchResultsView.as_view(), name="search_results"),
    path("profile/<int:registrikood>", ou_profile_view, name="profile"),
]
