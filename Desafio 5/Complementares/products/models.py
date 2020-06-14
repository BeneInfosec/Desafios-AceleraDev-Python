from django.db import models

# Create your models here.
class Category(models.Model): #Criação de alguns produtos dentro de algumas categorias
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descrição')

    def __str__(self):
        return f'{self.name} - {self.products.count()}'

class Product(models.Model): #Criação de um produto
    name = models.CharField('Nome', max_length=100) #max é obrigatorio
    description = models.TextField('Descrição')
    price = models.DecimalField('Preço', max_digits=8, decimal_places=2) #Contar 2 digitos decimais + 6 digitos antes da virgula
    category = models.ForeignKey(Category, on_delete=models.deletion.DO_NOTHING, related_name="products") # Uma categoria pode ter varios produtos

    def __str__(self): #Converter para string
        return self.name
