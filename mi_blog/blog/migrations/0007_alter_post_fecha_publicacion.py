# Generated by Django 4.1.6 on 2023-02-05 13:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0006_usuario"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="fecha_publicacion",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
