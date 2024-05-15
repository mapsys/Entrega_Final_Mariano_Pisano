from django.shortcuts import get_object_or_404, render
from .models import Intercambio, Mensaje

def mensajes_list(request):
    # Obtener los intercambios donde user_1 es el usuario actual
    intercambios = Intercambio.objects.filter(user_1=request.user).union(
                            Intercambio.objects.filter(user_2=request.user)
    )
 
    return render(request, 'mensajes/mensajes_list.html', {'intercambios': intercambios})

def detalle_conversacion(request, intercambio_id):
    intercambio = get_object_or_404(Intercambio, id=intercambio_id)
    mensajes = Mensaje.objects.filter(chat=intercambio).order_by('fecha_hora_enviado')
    return render(request, 'mensajes/detalle_conversacion.html', {'intercambio': intercambio, 'mensajes': mensajes})