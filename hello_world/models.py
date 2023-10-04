from django.db import models

class Estudio(models.Model):
    #id = models.IntegerField(primary_key=True)
    estudio = models.TextField()


class Pelicula(models.Model):
    #id = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=200)
    anio = models.IntegerField()
    pais = models.TextField()
    estreno = models.TextField()
    descripcion = models.TextField()
    duracion = models.IntegerField()
    gross = models.CharField(max_length=500)
    velimasen = models.CharField(max_length=500)
    estudio = models.ForeignKey(Estudio,on_delete=models.CASCADE)
    
class Genero(models.Model):
    #id = models.IntegerField(primary_key=True)
    id_peli = models.ForeignKey(Pelicula,on_delete=models.CASCADE)
    genero = models.TextField()

class Persona(models.Model):
    #Persona_id = models.IntegerField(primary_key=True)
    Nombre = models.TextField()
    Fecha_Nac = models.DateField()
    Pais = models.TextField()
    Url_imagen = models.ImageField()

class Clasificacion(models.Model)
   # id_clas= models.IntegerField(primary_key=True)
    clasificacion = models.TextField()

class Resena(models.Model):
    #id_res = models.IntegerField(primary_key=True)
    texto = models.TextField()
    calificacion = models.IntegerField()

class Usuario(models.Model):
   # id_user = models.IntegerField(primary_key=True)
    nombres = models.TextField()
    correo = models.TextField()
