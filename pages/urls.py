from django.urls import path
from .views import FormPageView, HomePageView, AboutPageView, SearchResultsView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("form/", FormPageView, name="form"),
    path("search/", SearchResultsView.as_view(), name="search_results"),
]
