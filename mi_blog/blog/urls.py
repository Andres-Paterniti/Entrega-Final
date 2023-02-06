from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from blog.views import (ProfileUpdateView)

from . import views

urlpatterns = [
    path('<int:id>/', views.detalle, name='detalle'),
    path('editar-perfil/', ProfileUpdateView.as_view(), name="editar_perfil"),


]