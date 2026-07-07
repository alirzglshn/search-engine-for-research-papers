from django.urls import path

from papers import views

app_name = "papers"

urlpatterns = [
    path("", views.home, name="home"),
    path("search/", views.search_results, name="search_results"),
]