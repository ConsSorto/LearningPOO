from django.db import models

# Create your models here.
class Person(models.Model):
    firstName = models.CharField(max_length=255, verbose_name='Nombre')
    lastName = models.CharField(max_length=255, verbose_name='Apellido')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado en')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Actualizado en')

    def __str__(self):
        return self.firstName + ' ' + self.lastName

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
