from datetime import datetime
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from .models import Post, Usuario
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from blog.forms import PostFormulario, UserRegisterForm, UserUpdateForm, AvatarFormulario
from django.contrib.auth.views import LogoutView
from django.contrib.auth.models import User
# Create your views here.

def frontpage (request):
    posts = Post.objects.all()
    return render (request, "blog/frontpage.html", {"posts": posts})


def about (request):
    return render(request, "blog/about.html")

@login_required
def detalle(request, id):
    post = Post.objects.get(id=id)
    contexto = {
        'post': post
    }
    return render(
        request=request,
        template_name='blog/detalle.html',
        context=contexto,
    )

def buscar (request):
    
    query = request.GET.get('query', '')

    posts = Post.objects.filter(Q(titulo__icontains=query) | Q(intro__icontains=query) | Q(texto__icontains=query))

    return render(request, 'blog/buscar.html', {'posts': posts, 'query': query})


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['categoria', 'titulo', 'intro', 'texto', 'fecha_publicacion', 'imagen']
    success_url = reverse_lazy('frontpage')
    template_name = "blog/post_form.html"

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['categoria','titulo', 'intro', 'texto', 'imagen']
    success_url = reverse_lazy('frontpage')
    template_name = "blog/post_editar.html"


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('frontpage')
    template_name = "blog/eliminar_post.html"



class UsuarioListView(LoginRequiredMixin, ListView):
    model = Usuario
    template_name = "blog/lista_usuarios.html"



class UsuarioCreateView(LoginRequiredMixin, CreateView):
    model = Usuario
    fields = ['nombre', 'apellido', 'dni', 'email']
    success_url = reverse_lazy('lista_usuarios')
    template_name = "blog/formulario_usuario.html"


class UsuarioDetailView(LoginRequiredMixin, DetailView):
    model = Usuario
    success_url = reverse_lazy('lista_usuarios')
    template_name = "blog/ver_usuario.html"


class UsuarioUpdateView(LoginRequiredMixin, UpdateView):
    model = Usuario
    fields = ['nombre', 'apellido', 'dni', 'email']
    success_url = reverse_lazy('lista_usuarios')
    template_name = "blog/formulario_usuario.html"


class UsuarioDeleteView(LoginRequiredMixin, DeleteView):
    model = Usuario
    success_url = reverse_lazy('lista_usuarios')
    template_name = "blog/confirmar_eliminacion_usuario.html"


def registro(request):
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)

        if formulario.is_valid():
            formulario.save()  # Esto lo puedo usar porque es un model form
            url_exitosa = reverse('frontpage')
            return redirect(url_exitosa)
    else:  # GET
        formulario = UserRegisterForm()
    return render(
        request=request,
        template_name='blog/registro.html',
        context={'form': formulario},
    )


def login_view(request):
    next_url = request.GET.get('next')
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data
            usuario = data.get('username')
            password = data.get('password')
            user = authenticate(username=usuario, password=password)
            # user puede ser un usuario o None
            if user:
                login(request=request, user=user)
                if next_url:
                    return redirect(next_url)
                url_exitosa = reverse('frontpage')
                return redirect(url_exitosa)
    else:  # GET
        form = AuthenticationForm()
    return render(
        request=request,
        template_name='blog/login.html',
        context={'form': form},
    )



class CustomLogoutView(LogoutView):
    template_name = 'blog/logout.html'


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('frontpage')
    template_name = 'blog/formulario_perfil.html'

    def get_object(self, queryset=None):
        return self.request.user

def agregar_avatar(request):
    if request.method == "POST":
        formulario = AvatarFormulario(request.POST, request.FILES) # Aquí me llega toda la info del formulario html

        if formulario.is_valid():
            avatar = formulario.save()
            avatar.user = request.user
            avatar.save()
            url_exitosa = reverse('inicio')
            return redirect(url_exitosa)
    else:  # GET
        formulario = AvatarFormulario()
    return render(
        request=request,
        template_name='estudiantes/formulario_avatar.html',
        context={'form': formulario},
    )
