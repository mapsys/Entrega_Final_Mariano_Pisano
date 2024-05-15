from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from . import models, forms

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

class PosteoDetail(LoginRequiredMixin, DetailView):
    model = models.Posteo

class PosteoCreate(LoginRequiredMixin, CreateView):
    model = models.Posteo
    form_class = forms.PosteoForm
    success_url = reverse_lazy("posteos:home")

class NuevoPostView(LoginRequiredMixin, CreateView):
    model         = models.Posteo
    template_name = 'posteos/posteo_form.html'
    success_url   = '/posteos/'
    fields        = ['titulo', 'subtitulo', 'contenido', 'imagen']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)