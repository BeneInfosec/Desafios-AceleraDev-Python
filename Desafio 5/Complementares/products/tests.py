from django.test import TestCase
from .models import Product
# Create your tests here.

class ProductStrTestCase(TestCase):
    def test_str_should_return_name(self):
        #Product.objects.list_from_category('exemplo') # Faz a lista com filtros prontos
        product = Product.objects.create(
            name = 'Teste Produto',
            description= 'Teste description',
            price = 10.5
        )

        self.assertEqual(str(product), 'Teste Produto')
