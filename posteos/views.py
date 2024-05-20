from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from . import models, forms
from django.contrib import messages
'''
Vista funcion para ver el listado de posteos existentes'''
# Create your views here.
@login_required
def posteo_list(request):
    consulta = request.GET.get("consulta", None)
    if consulta:
        print(consulta)
        query = models.Posteo.objects.filter(titulo__icontains=consulta)
    else:
        query = models.Posteo.objects.all()
    context = {"posts": query}
    return render(request, "posteos/posteo_list.html", context)

'''
Vista de clase que permite ver el detalle de un posteo'''
class PosteoDetail(LoginRequiredMixin, DetailView):
    model = models.Posteo

'''
Vista de clase que permite crear un nuevoi posteo'''
class NuevoPostView(LoginRequiredMixin, CreateView):
    model         = models.Posteo
    template_name = 'posteos/posteo_form.html'
    success_url   = '/posteos/'
    fields        = ['titulo', 'subtitulo', 'contenido', 'imagen']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
'''
Vista funcion que permite buscar un posteo'''
@login_required  
def buscar_posts(request):
    titulo = request.GET.get('titulo', None)

    if titulo:
        posts = models.Posteo.objects.filter(titulo__icontains=titulo)
    else:
        posts = models.Posteo.objects.all()

    posts = posts.order_by('id')

    formulario_buscar_posts = forms.FormularioBuscarPosts()

    return render(request, 'posteos/buscar_posteos.html', { 'form' : formulario_buscar_posts, 'posts' : posts })

@login_required
def confirmar_eliminacion(request, posteo_id):
    posteo = get_object_or_404(models.Posteo, id=posteo_id)
    return render(request, 'posteos/confirmar_eliminacion.html', {'posteo': posteo})

@login_required
def borrar_posteo(request, posteo_id):
    posteo = get_object_or_404(models.Posteo, id=posteo_id)
    
    if request.method == 'POST':
        if request.user == posteo.autor:
            posteo.delete()
            messages.success(request, 'Post eliminado correctamente.')
        else:
            messages.error(request, 'No tienes permisos para eliminar este post.')
        return redirect('posteos:home')  # Asegúrate de usar la URL correcta para listar los posteos
    
    return render(request, 'posteos/confirmar_eliminacion.html', {'posteo': posteo})