from django.contrib import admin
from .models import (Product, Cart_items, Phones,
                     Camera, Accessories, Tv, Printers,
                     Refrigerators, Microwaves, Computers,
                     Mobiles, Smarts, Diys, Homes, Powers,
                     Electronics, Electrical,Laptops,
                     Appliances, Trending, Available,
                     Photos, Pixels, Fans, Alx, Order, Contacts)

# Register your models here.
admin.site.register(Product)
admin.site.register(Cart_items)
admin.site.register(Phones)
admin.site.register(Camera)
admin.site.register(Accessories)
admin.site.register(Tv)
admin.site.register(Printers)
admin.site.register(Refrigerators)
admin.site.register(Microwaves)
admin.site.register(Computers)
admin.site.register(Mobiles)
admin.site.register(Smarts)
admin.site.register(Diys)

#CATEGORIES
admin.site.register(Homes)
admin.site.register(Powers)
admin.site.register(Electronics)
admin.site.register(Electrical)

#LAPTOPS
admin.site.register(Laptops)
admin.site.register(Appliances)

#SMARTPHONES
admin.site.register(Trending)
admin.site.register(Available)


#CAMERAS
admin.site.register(Photos)
admin.site.register(Pixels)

#ACCESSORIES
admin.site.register(Fans)
admin.site.register(Alx)

#CONTACT
admin.site.register(Contacts)









