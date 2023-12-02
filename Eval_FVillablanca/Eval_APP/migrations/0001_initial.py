# Generated by Django 4.2.6 on 2023-12-02 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Socio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('fecha_incorporacion', models.DateField()),
                ('fecha_nacimiento', models.DateField()),
                ('telefono', models.CharField(max_length=15)),
                ('correo_electronico', models.EmailField(max_length=254)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=1)),
                ('estado', models.CharField(choices=[('V', 'Vigente'), ('S', 'Suspendido'), ('R', 'Retirado')], max_length=1)),
                ('observacion', models.TextField(blank=True)),
            ],
        ),
    ]
