from django.urls import path
from .views import FormularioTemplate


urlpatterns = [
    path('', FormularioTemplate, name='formulario'),
]
