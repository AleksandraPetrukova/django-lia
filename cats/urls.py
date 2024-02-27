from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="cats"),
    path("<int:cat_id>/", views.cat_details, name="cat"),
    path("add_cat/", views.add_cat, name="add_cat"),
    path("search/", views.search_cat, name="search_cat"),
]