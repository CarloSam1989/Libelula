from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='categorias/', null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    activa = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_disponible = models.IntegerField()
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='media/',null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    destacado = models.BooleanField(default=False)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    en_oferta = models.BooleanField(default=False)
    fecha_inicio_oferta = models.DateField(null=True, blank=True)
    fecha_fin_oferta = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nombre

class Inventario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.producto.nombre} - {self.categoria.nombre}"
