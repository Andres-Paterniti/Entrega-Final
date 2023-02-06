from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.






class Post(models.Model):
    titulo = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    texto = models.TextField()
    fecha_publicacion = models.DateTimeField(default=timezone.now)
    imagen = models.ImageField(upload_to="repositorio/", blank=True, null=True)
    categoria = models.CharField(max_length=255)



    class Meta:
        ordering = ('-fecha_publicacion',)


    def __str__(self):
        return f"{self.titulo}"


class Usuario(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    dni = models.CharField(max_length=32)
    email = models.EmailField()
    fecha_nacimiento = models.DateField(null=True)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"



class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)

    def __str__(self):
        return f"Imagen de: {self.user}"
