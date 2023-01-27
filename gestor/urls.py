from . import views

from django.urls import path

urlpatterns = [
    path("", views.home,name="home"),
    path("registroCurso/",views.registroCurso),
    path("eliminacionCurso/<codigo>",views.eliminacionCurso)
]
