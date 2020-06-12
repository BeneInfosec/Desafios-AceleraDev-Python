from django.db import models

# Create your models here.

class Product(models.Model): #Criação de um produto
    name = models.CharField('Nome', max_length=100) #max é obrigatorio
    description = models.TextField('Descrição')
    price = models.DecimalField('Preço', max_digits=8, decimal_places=2) #Contar 2 digitos decimais + 6 digitos antes da virgula

    def __str__(self): #Converter para string
        return self.name
