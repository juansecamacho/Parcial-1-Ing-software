from django.shortcuts import render, redirect
from .forms import FlightForm
from .models import Flight
from django.db.models import Avg, Count

def index(request):
    return render(request, 'index.html')

def registrar_vuelo(request):
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_vuelos')
    else:
        form = FlightForm()
    return render(request, 'registrar_vuelo.html', {'form': form})

def listar_vuelos(request):
    vuelos = Flight.objects.all().order_by('-precio')
    return render(request, 'listar_vuelos.html', {'vuelos': vuelos})

def estadisticas_vuelos(request):
    stats = {
        'total_nacional': Flight.objects.filter(tipo='Nacional').count(),
        'total_internacional': Flight.objects.filter(tipo='Internacional').count(),
        'promedio_precio_nacional': Flight.objects.filter(tipo='Nacional').aggregate(Avg('precio'))['precio__avg']
    }
    return render(request, 'estadisticas_vuelos.html', {'stats': stats})
