"""mi_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from blog.views import (frontpage, about, detalle, buscar,registro, login_view, agregar_avatar, PostCreateView, 
                        PostUpdateView,PostDeleteView,UsuarioListView,UsuarioCreateView,
                        UsuarioDetailView, UsuarioUpdateView,UsuarioDeleteView,CustomLogoutView,ProfileUpdateView)

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("about/", about, name="about"),
    path("buscar/", buscar, name="buscar"),
    path('<int:id>/', detalle, name="detalle"),
    path("", frontpage, name="frontpage"),
    #los urls para los usuarios
    path('lista-usuario/',UsuarioListView.as_view(), name="lista_usuarios"), 
    path('crear-usuario/',UsuarioCreateView.as_view(), name="crear_usuario"),
    path('detalle-usuario/<int:pk>',UsuarioDetailView.as_view(), name="ver_usuario"),
    path('editar-usuario/<int:pk>/',UsuarioUpdateView.as_view(), name="editar_usuario"),
    path('eliminar-usuario/<int:pk>/',UsuarioDeleteView.as_view(), name="eliminar_usuario"),
    #urls para los post
    path('crear-post/',PostCreateView.as_view(), name="crear_post"),
    path('editar-post/<int:pk>/',PostUpdateView.as_view(), name="editar_post"),
    path('eliminar-post/<int:pk>/',PostDeleteView.as_view(), name="eliminar_post"),
    #inicio de sesion y registro
    path('registro/', registro, name="registro"),
    path('login/', login_view, name="login"),
    path('logout/', CustomLogoutView.as_view(), name="logout"),
    #url de perfil
    path('<slug:slug>editar-perfil/', ProfileUpdateView.as_view(), name="editar_perfil"),
    path('agregar-avatar/', agregar_avatar, name="agregar_avatar"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
