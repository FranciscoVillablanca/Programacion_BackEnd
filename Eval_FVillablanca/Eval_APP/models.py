from django.db import models

class Socio(models.Model):
    nombre = models.CharField(max_length=80)
    fecha_incorporacion = models.DateField()
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=15)
    correo_electronico = models.EmailField()
    sexo = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Femenino')])
    estados = [('V', 'Vigente'), ('S', 'Suspendido'), ('R', 'Retirado')]
    estado = models.CharField(max_length=1, choices=estados)
    observacion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre