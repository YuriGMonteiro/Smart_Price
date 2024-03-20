from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    token = models.CharField(max_length=100)
    
    def __str__(self):
        return self.email
    
    
class Products(models.Model):
    id_produto = models.IntegerField()
    id_usuario = models.IntegerField()
    codigo = models.CharField(max_length=50)
    descricao = models.TextField()
    situacao = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=15, decimal_places=2)
    preco_custo = models.DecimalField(max_digits=15, decimal_places=2)
    estoque_atual = models.IntegerField()
    
    class Meta:
        db_table = "product"