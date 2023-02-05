from django.shortcuts import render
from .forms import AddressForm


def FormularioTemplate(request):
    form = AddressForm(request.POST, request.FILES, None)
    return render(request, 'formulario/formulario.html', {'form': form })
