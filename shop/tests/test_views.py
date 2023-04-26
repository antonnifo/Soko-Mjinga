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

