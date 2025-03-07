from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    old_price = models.FloatField()
    image = models.ImageField(upload_to='products/')  # Ensure correct upload path

    def __str__(self):
        return self.name

class Cart_items(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)  # Use ForeignKey
    quantity = models.IntegerField()

    def total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

class Phones(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    old_price = models.FloatField()
    image = models.ImageField(upload_to='phones/')  # Ensure correct upload path

    def __str__(self):
        return self.name

class Camera(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    old_price = models.FloatField()
    image = models.ImageField(upload_to='cameras/')

    def __str__(self):
        return self.name


class Accessories(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    old_price = models.FloatField()
    image = models.ImageField(upload_to='accessories/')

    def __str__(self):
        return self.name

class Tv(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    old_price = models.FloatField()
    image = models.ImageField(upload_to='tv/')

    def __str__(self):
        return self.name

class Printers(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    old_price = models.FloatField()
    image = models.ImageField(upload_to='printers/')

    def __str__(self):
        return self.name

class Refrigerators(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    old_price = models.FloatField()
    image = models.ImageField(upload_to='Refrigerators/')

    def __str__(self):
        return self.name

class  Microwaves(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    old_price = models.FloatField()
    image = models.ImageField(upload_to='Microwaves/')

    def __str__(self):
        return self.name

class  Computers(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    old_price = models.FloatField()
    image = models.ImageField(upload_to='Computers/')

    def __str__(self):
        return self.name

class  Mobiles(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    old_price = models.FloatField()
    image = models.ImageField(upload_to='Mobiles/')

    def __str__(self):
        return self.name


class  Smarts(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    old_price = models.FloatField()
    image = models.ImageField(upload_to='Smarts/')

    def __str__(self):
        return self.name

class  Diys(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    old_price = models.FloatField()
    image = models.ImageField(upload_to='Diys/')

    def __str__(self):
        return self.name

#CATEGORIES

class  Homes(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    old_price = models.FloatField()
    image = models.ImageField(upload_to='Homes/')

    def __str__(self):
        return self.name


class  Powers(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    old_price = models.FloatField()
    image = models.ImageField(upload_to='Powers/')

    def __str__(self):
        return self.name


class  Electrical(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    old_price = models.FloatField()
    image = models.ImageField(upload_to='Electrical/')

    def __str__(self):
        return self.name

class  Electronics(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    old_price = models.FloatField()
    image = models.ImageField(upload_to='Electronics/')

    def __str__(self):
        return self.name

#LAPTOPS

class Laptops(models.Model):  # ✅ Ensure the class name is 'Laptops'
    name = models.CharField(max_length=100)
    price = models.FloatField()
    old_price = models.FloatField()
    image = models.ImageField(upload_to='Laptops/')

    def __str__(self):
        return self.name

class  Appliances(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    old_price = models.FloatField()
    image = models.ImageField(upload_to='Appliances/')

    def __str__(self):
        return self.name


#SMARTPHONES

class Trending(models.Model):  # ✅ Ensure the class name is 'Laptops'
    name = models.CharField(max_length=100)
    price = models.FloatField()
    old_price = models.FloatField()
    image = models.ImageField(upload_to='Trending/')

    def __str__(self):
        return self.name

class  Available(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    old_price = models.FloatField()
    image = models.ImageField(upload_to='Available/')

    def __str__(self):
        return self.name


#CAMERAS

class Photos(models.Model):  # ✅ Ensure the class name is 'Laptops'
    name = models.CharField(max_length=100)
    price = models.FloatField()
    old_price = models.FloatField()
    image = models.ImageField(upload_to='Photos/')

    def __str__(self):
        return self.name

class  Pixels(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    old_price = models.FloatField()
    image = models.ImageField(upload_to='Pixels/')

    def __str__(self):
        return self.name


#CAMERAS

class Fans(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    old_price = models.FloatField()
    image = models.ImageField(upload_to='Fans/')

    def __str__(self):
        return self.name

class  Alx(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    old_price = models.FloatField()
    image = models.ImageField(upload_to='Alx/')

    def __str__(self):
        return self.name

def get_default_user():
        return User.objects.first().id  # Returns the first user in the database

def get_default_product():
        return Product.objects.first().id  # Returns the first product in the database

class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.TextField()
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    telephone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order by {self.first_name} {self.last_name}"

# CONTACT SECTION
class Contacts(models.Model):
    contact_name = models.CharField(max_length=100)
    contact_email = models.EmailField(max_length=100)
    contact_phone = models.IntegerField()
    contact_message = models.TextField()

    def __str__(self):
        return self.contact_name








