from django.db import models

class Estudio(models.Model):
    estudio = models.TextField()

    def __str__(self):
        return self.estudio

class Genero(models.Model):
    genero = models.TextField()
    
    def __str__(self):
        return self.genero

class Persona(models.Model):
    Nombre = models.TextField()
    Fecha_Nac = models.DateField()
    Pais = models.TextField()
 #   Url_imagen = models.ImageField()
    
class Pelicula(models.Model):
    titulo = models.CharField(max_length=200)
    anio = models.IntegerField()
    pais = models.TextField()
    estreno = models.TextField()
    descripcion = models.TextField()
    duracion = models.IntegerField()
    gross = models.CharField(max_length=500)
    velimasen = models.CharField(max_length=500)
    estudio = models.ForeignKey(Estudio,on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero,on_delete=models.CASCADE)
    
class Rol(models.Model):
    pelicula = models.ForeignKey(Pelicula,on_delete=models.CASCADE)   
    persona = models.ForeignKey(Persona,on_delete=models.CASCADE)  
    
class Clasificacion(models.Model):
    clasificacion = models.TextField()

class Usuario(models.Model):
    nombres = models.TextField()
    correo = models.TextField()

class Resena(models.Model):
    texto = models.TextField()
    calificacion = models.IntegerField()
    pelicula = models.ForeignKey(Pelicula,on_delete=models.CASCADE)   
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)   

#class Seguidor(models.Model):
#    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)   
