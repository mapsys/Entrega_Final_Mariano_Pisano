from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Intercambio, Mensaje
from django.contrib.auth.models import User
from .forms import NuevoIntercambioForm
from django.db import models
from django.contrib import messages

'''
Vista funcion quye muestra la lista de mensajes
donde un usuario esta involucrado'''
@login_required
def mensajes_list(request):
    # Obtener los intercambios donde user_1 es el usuario actual
    intercambios = Intercambio.objects.filter(user_1=request.user).union(
                            Intercambio.objects.filter(user_2=request.user)
    )
 
    return render(request, 'mensajes/mensajes_list.html', {'intercambios': intercambios})

'''
Vista funcion que muestra los mensajes dentro de un intercambio'''
@login_required
def detalle_conversacion(request, intercambio_id):
    intercambio = get_object_or_404(Intercambio, id=intercambio_id)
    mensajes = Mensaje.objects.filter(chat=intercambio).order_by('fecha_hora_enviado')
    return render(request, 'mensajes/detalle_conversacion.html', {'intercambio': intercambio, 'mensajes': mensajes})

'''
Vista funcion que permite agregar un nuevo mensaje a un intercambio
'''
def nuevo_mensaje(request, intercambio_id):
    if request.method == 'POST':
        mensaje_texto = request.POST.get('mensaje')
        intercambio = get_object_or_404(Intercambio, id=intercambio_id)
        Mensaje.objects.create(
            chat=intercambio,
            de_user=request.user,
            mensaje=mensaje_texto
        )
        return redirect('mensajes:detalle_conversacion', intercambio_id=intercambio_id)
'''
Vista Funcion que permite iniciar un nuevo intercambio de mensajes
'''
@login_required
def iniciar_conversacion(request):
    if request.method == 'POST':
        form = NuevoIntercambioForm(request.POST, user=request.user)
        if form.is_valid():
            user_id = form.cleaned_data['user_id'].id
            if user_id != request.user.id:
                # Verificar si ya existe un intercambio con el usuario seleccionado
                intercambio = Intercambio.objects.filter(
                    (models.Q(user_1=request.user) & models.Q(user_2_id=user_id)) |
                    (models.Q(user_1_id=user_id) & models.Q(user_2=request.user))
                ).first()

                if not intercambio:
                    # Crear un nuevo intercambio si no existe
                    user_destino = get_object_or_404(User, id=user_id)
                    intercambio = Intercambio.objects.create(
                        user_1=request.user,
                        user_2=user_destino
                    )

                return redirect('mensajes:detalle_conversacion', intercambio_id=intercambio.id)
    else:
        form = NuevoIntercambioForm(user=request.user)

    return render(request, 'mensajes/iniciar_conversacion.html', {'form': form})

@login_required
def confirmar_eliminacion(request, intercambio_id):
    intercambio = get_object_or_404(Intercambio, id=intercambio_id)
    return render(request, 'mensajes/confirmar_eliminacion.html', {'intercambio': intercambio})
@login_required
def borrar_intercambio(request, intercambio_id):
    intercambio = get_object_or_404(Intercambio, id=intercambio_id)
    
    if request.method == 'POST':
        if request.user == intercambio.user_1 or request.user == intercambio.user_2:
            intercambio.delete()
            messages.success(request, 'Intercambio borrado correctamente.')
        else:
            messages.error(request, 'No tienes permisos para borrar este intercambio.')
        return redirect('mensajes:home')  # Asegúrate de usar la URL correcta para listar las conversaciones
    
    return render(request, 'mensajes/confirmar_eliminacion.html', {'intercambio': intercambio})
