from django.test import TestCase
from django.urls import reverse  
from django.utils import timezone
from shop.models import Product, Category



class ProductListViewTests(TestCase):

    def test_template_name_correct(self):  
        response = self.client.get(reverse("shop:product_list"))
        self.assertTemplateUsed(response, "shop/product/list.html")

    def test_template_content(self):
        response = self.client.get(reverse("shop:product_list"))
        self.assertContains(response, "<h3>Categories</h3>")
        self.assertNotContains(response, "Not on the page")

class ProductDetailViewTests(TestCase):

    def setUp(self):   
        self.category = Category.objects.create(name="Electronics",slug="electronics")
        self.product = Product.objects.create(name="JBL SoundBar",slug ="jbl-soundbar",description="5.1 Channel",\
                                    category=self.category,
                                    price=99.99)  
        
        self.products_by_category = self.category.products.all()

    def test_template_name_correct(self):  
        response = self.client.get(reverse("shop:product_detail", args=[self.product.id,\
                                                                      self.product.slug]))
        self.assertTemplateUsed(response, "shop/product/detail.html")

    def test_template_content(self):
        response = self.client.get(reverse("shop:product_detail", args=[self.product.id,\
                                                                      self.product.slug]))
        self.assertContains(response, "Ksh")
        self.assertNotContains(response, "No he")

