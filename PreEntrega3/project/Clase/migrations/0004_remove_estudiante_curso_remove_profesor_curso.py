# Generated by Django 5.0.4 on 2024-04-29 23:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Clase', '0003_comision_curso_alter_comision_nombre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudiante',
            name='curso',
        ),
        migrations.RemoveField(
            model_name='profesor',
            name='curso',
        ),
    ]
