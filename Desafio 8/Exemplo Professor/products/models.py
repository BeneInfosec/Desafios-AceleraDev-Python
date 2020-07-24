"""
    Modelos do app de Produtos
"""

from django.db import models
from django.db.models import Q, QuerySet



class ProductManager(models.Manager):
    #Filtro simples
    def with_text(self, text: str) -> QuerySet: 
        """
            Realiza a pesquisa nos produtos cujo nome contenha "text"
        """
        queryset = self.get_queryset().filter(name__contains = text)
        return queryset
    
    def expensive_products(self) -> QuerySet:
        """
        Realiza o filtro dos produtos cujo preço seja maior que 500 reais.
        """
        #Executa a queryset com o filtro maior ou igual a 500
        return self.get_queryset().filter(price__gte=500)

    def cheap_toys(self) -> QuerySet:
        """
            Retorna a lista com os brinquedos mais baratos.
        """
        return self.get_queryset().filter(
            category__name = 'Category',
            price__lte=2
        )
    
    def toys_or_expensive_item(self) -> QuerySet:
        """
            Retorna a lista dos brinquedos mais caros
        """
        query_filter = Q(category__name = 'Category') | Q(price__gte = 500)
        queryset = self.get_queryset().filter(query_filter)
        print(queryset.query)
        return queryset

    def test_function(self):
        a = self.with_text("")
        b = self.expensive_products()
        c = self.cheap_toys()
        d = self.toys_or_expensive_item()


# Create your models here.
class Category(models.Model): #Criação de alguns produtos dentro de algumas categorias
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descrição')

    def __str__(self):
        return f'{self.name} - {self.products.count()}'

    class Meta:
        verbose_name_plural = 'Categories'
        




class Product(models.Model): #Criação de um produto
    """
        Model contendo todos os campos necessários para cadastrar produtos no ecomm.
    """
    objects = ProductManager()
    name = models.CharField('Nome', max_length=100) #max é obrigatorio
    description = models.TextField('Descrição')
    price = models.DecimalField('Preço', max_digits=8, decimal_places=2) #Contar 2 digitos decimais + 6 digitos antes da virgula
    category = models.ForeignKey(Category, on_delete=models.deletion.DO_NOTHING, related_name="products") # Uma categoria pode ter varios produtos

    def __str__(self): #Converter para string
        return self.name




class Order(models.Model):
    name = models.CharField('Nome do cliente', max_length = 100)
    payment = models.CharField('Meio Pagamento', max_length = 50)
    products = models.ManyToManyField(Product)

    #Informacional
    @property
    def total_amount(self):
        return sum(product.price for product in self.products.all())

    def __str__(self):
        return f'{self.name} - {self.total_amount}'