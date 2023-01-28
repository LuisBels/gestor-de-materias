from . import views

from django.urls import path

urlpatterns = [
    path("", views.home,name="home"),
    path("registroCurso/",views.registroCurso),
    path("edicionCurso/<codigo>", views.edicionCurso),
    path("editarCurso/", views.editarCurso),
    path("eliminacionCurso/<codigo>",views.eliminacionCurso)
]
