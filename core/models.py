from django.db import models

class Sonho(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    emocao = models.CharField(max_length=100)
    tema = models.CharField(max_length=100)
    nivel_lucidez = models.IntegerField()
    data = models.DateField()
    duracao = models.DurationField()

    def __str__(self):
        return self.titulo

