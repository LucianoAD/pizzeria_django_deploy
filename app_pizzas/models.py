from django.db import models

class Pizza(models.Model):
    class Meta:
        db_table = "pizzeria_pizzas"
        
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='pizzas/')

    def __str__(self):
        return self.nombre
    
    def get_fields(self):
        return [
            (field.verbose_name, field.value_from_object(self))
            for field in self.__class__._meta.fields[1:]
        ]
