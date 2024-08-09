from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("brasil/", views.brasil, name="brasil"),
    path("estados_unidos/", views.estados_unidos, name="estados_unidos"),
    path("uniao_sovietica/", views.uniao_sovietica, name="uniao_sovietica"),
    path("japao/", views.japao, name="japao"),
    path("china/", views.estados_unidos, name="estados_unidos"),
    path("australia/", views.estados_unidos, name="estados_unidos"),
    path("italia/", views.estados_unidos, name="estados_unidos"),
    path("franca/", views.estados_unidos, name="estados_unidos"),
    path("alemanha/", views.estados_unidos, name="estados_unidos"),
    path("reino_unido/", views.estados_unidos, name="estados_unidos"),
    path("coreia_do_sul/", views.estados_unidos, name="estados_unidos"),
    path("canada/", views.estados_unidos, name="estados_unidos"),
]