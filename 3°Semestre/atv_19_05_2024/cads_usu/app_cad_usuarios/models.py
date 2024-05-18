from django.db import models

class Usuario(models.Model):
    id_usuario= models.AutoField(primary_key=True)
    nome=models.TextField(max_length=255)
    idade=models.IntegerField()
    gmail=models.EmailField(max_length=500)
    senha=models.CharField(max_length=100)

class Base_questoes(models.Model):
    Pergunta = models.CharField(max_length=200)

    def __str__(self):
        return self.Pergunta
    objects = models.Manager()


class Sub_questoes(models.Model):
    questao = models.ForeignKey(Base_questoes, on_delete=models.CASCADE)
    ops = models.CharField(max_length=200)
    voto = models.IntegerField(default=0)

    def __str__(self):
        return self.ops
class Quem_voto(models.Model):
    Nome=models.CharField(max_length=200)
    voto=models.CharField(max_length=200)