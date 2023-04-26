from django.test import TestCase
from django.urls import reverse, resolve
from shop.views import product_list, product_detail
from shop.models import Product, Category

class ProductListPageURLTests(TestCase):

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):  
        response = self.client.get(reverse("shop:product_list"))
        self.assertEqual(response.status_code, 200)

    def test_url_maps_right_view(self):
        url = reverse("shop:product_list")
        self.assertEquals(resolve(url).func, product_list)


class ProductListByCategoryPageURLTests(TestCase):

    def setUp(self):

        self.category = Category.objects.create(name="Electronics",slug="electronics")
        self.product = Product.objects.create(name="JBL SoundBar",slug ="jbl-soundbar",description="5.1 Channel",\
                                    category=self.category,
                                    price=99.99)  
        
        self.products_by_category = self.category.products.all() 

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/electronics/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):  
        response = self.client.get(reverse("shop:product_list_by_category", args=['electronics']))
        self.assertEqual(response.status_code, 200)

    def test_url_maps_right_view(self):
        url = reverse('shop:product_list_by_category' , args=['electronics'])
        self.assertEquals(resolve(url).func, product_list)
                            

class ProductDetailPageURLTests(TestCase):

    def setUp(self):   
        self.category = Category.objects.create(name="Electronics",slug="electronics")
        self.product = Product.objects.create(name="JBL SoundBar",slug ="jbl-soundbar",description="5.1 Channel",\
                                    category=self.category,
                                    price=99.99)  
        
        self.products_by_category = self.category.products.all() 
   
    # def test_url_exists_at_correct_location(self):
    #     response = self.client.get("/<self.product.id>/jbl-soundbar/")
    #     print(self.product.id)
    #     self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):  
        response = self.client.get(reverse("shop:product_detail", args=[self.product.id,\
                                                                      self.product.slug]))                                                             
        self.assertEqual(response.status_code, 200)

    def test_url_maps_right_view(self):
        url = reverse('shop:product_detail' , args=[self.product.id,\
                                                    self.product.slug])
        self.assertEquals(resolve(url).func, product_detail)