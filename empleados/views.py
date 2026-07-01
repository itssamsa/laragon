from django.shortcuts import render, redirect
from .models import Empleado
from .forms import EmpleadoForm


def lista_empleados(request):
    empleados = Empleado.objects.all()

    return render(request, 'empleados/lista.html', {
        'empleados': empleados
    })


def crear_empleado(request):

    if request.method == 'POST':
        form = EmpleadoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('lista')

    else:
        form = EmpleadoForm()

    return render(request, 'empleados/crear.html', {
        'form': form
    })