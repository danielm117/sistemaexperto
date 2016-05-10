from django.db import models
from django.utils.encoding import uri_to_iri

class Usuario(models.Model):
    fecha_nacimiento = models.DateField()
    nombres = models.CharField(max_length=50)
    correo = models.EmailField()
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    estatura= models.IntegerField();
    ejercicio = models.IntegerField();
    genero = models.CharField(max_length=1)
    contrasena = models.CharField(max_length=30)
    def __unicode__(self):
        return unicode(self.email)
