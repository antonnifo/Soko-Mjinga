from django.test import TestCase
from django.urls import reverse, resolve
from shop.models import Product, Category

class ModelsTestCase(TestCase):
    def setUp(self):   
        self.category = Category.objects.create(name="Electronics",slug="electronics")
        self.product = Product.objects.create(name="JBL SoundBar",slug ="jbl-soundbar",description="5.1 Channel",\
                                    category=self.category,
                                    price=99.99)  
        
        self.products_by_category = self.category.products.all()      

    def test_category_creation(self):
        self.assertTrue(isinstance(self.category, Category))
        self.assertEqual(self.category.__str__(), self.category.name)

    def test_product_creation(self):
        self.assertTrue(isinstance(self.product, Product))
        self.assertEqual(self.product.__str__(), self.product.name)

