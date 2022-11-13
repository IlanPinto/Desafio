from django.urls import path
from MiApp.views import mostrar_familiares
urlpatterns = [
    path('familiares/', mostrar_familiares),
]