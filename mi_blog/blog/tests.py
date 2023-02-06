from django.test import TestCase

from blog.models import Post


class PostTests(TestCase):


    def test_creacion_de_publicacion(self):
        """
        Prueba crear post con titulo cortos y largos
        """
        post_nombre_valido = Post.objects.create(
            nombre="nombre corto", categoria=101
        )
        # Compruebo que la publiacacion fue creada
        self.assertEqual(Post.objects.all().count(), 1)
        self.assertIsNotNone(post_nombre_valido.id)
