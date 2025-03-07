from django.urls import path
from .import views
from trendy_kart.views import add_to_cart,remove_from_cart


urlpatterns =(
    path('', views.index, name='index'),
    path('product/', views.product, name='product'),
    path('checkout/', views.checkout, name='checkout'),
    path('blank/', views.blank, name='blank'),
    path('store/', views.store, name='store'),
    path('layout/', views.layout, name='layout'),
    path('accessories/', views.accessories, name='accessories'),
    path('camera/', views.camera, name='camera'),
    path('categories/', views.categories, name='categories'),
    path('deals/', views.deals, name='deals'),
    path('laptops/', views.laptop, name='laptops'),
    path('phones/', views.phones, name='phones'),
    path('contacts/', views.contacts, name='contacts'),
    path('newsletter_subscriptions/', views.newsletter_subscriptions, name='newsletter_subscriptions'),
    path('cart/', views.cart, name='cart'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('store/', views.store, name='store'),
    path('search/', views.search, name='search'),
    path('checkout/', views.checkout, name='checkout'),
    path("cart/remove/<int:product_id>/", views.remove_from_cart, name="remove_from_cart"),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout, name='logout'))



