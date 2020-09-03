from django.test import TestCase
from .models import Product, Category
# Create your tests here.

class ProductStrTestCase(TestCase):
    def test_str_should_return_name(self):
        category = Category.objects.create(name='cat1', description='cat1 desc')
        product = Product.objects.create(
            name = 'Teste Produto',
            description = 'Teste description',
            price = 10.5,
            category=category
        )

        self.assertEqual(str(product), 'Teste Produto')

        #Product.objects.list_from_category('exemplo') # Faz a lista com filtros prontos
