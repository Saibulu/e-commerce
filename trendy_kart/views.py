from django.contrib.admin.templatetags.admin_list import results
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import (Product, Cart_items, Phones,
                     Camera, Accessories, Tv,
                     Microwaves, Refrigerators,
                     Printers, Computers,
                     Mobiles, Smarts, Diys,
                     Homes, Powers,
                     Electrical, Electronics, Laptops,
                     Appliances, Trending, Available,
                     Photos, Pixels, Fans, Alx)
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):

    microwaves = Microwaves.objects.all()
    refrigerators = Refrigerators.objects.all()
    printers = Printers.objects.all()
    tv = Tv.objects.all()
    products = Product.objects.all()
    phone = Phones.objects.all()
    cameras = Camera.objects.all()
    accessory = Accessories.objects.all()
    context = {
        'microwaves': microwaves,
        'refrigerators': refrigerators,
        'printers': printers,
        'tv': tv,
        'camera': cameras,
        'accessories': accessory,
        'phones': phone,
        'products': products
    }

    return render(request, 'index.html', context)



def product(request):
    return render(request, 'product.html')


def checkout(request):
    return render(request, "checkout.html")


def blank(request):
    return render(request, 'blank.html')


def store(request):
    return render(request, 'store.html')


def layout(request):
    return render(request, 'layout.html')


def accessories(request):
   fan =Fans.objects.all()
   alx = Alx.objects.all()
   context ={
       'fans': fan,
       'alx': alx
    }
   return render(request, 'accessories.html', context)


def camera(request):
    photos = Photos.objects.all()
    pixels= Pixels.objects.all()
    context ={
        'photos': photos,
        'pixels': pixels
    }
    return render(request, 'camera.html', context)


def categories(request):
    power =Powers.objects.all()
    electrical = Electrical.objects.all()
    electronic = Electronics.objects.all()
    homes = Homes.objects.all()
    context ={
        'powers': power,
        'electrical': electrical,
        'electronic': electronic,
        'homes': homes
    }
    return render(request, 'categories.html', context)


def deals(request):
    mobile = Mobiles.objects.all()
    smart = Smarts.objects.all()
    diy = Diys.objects.all()
    computer = Computers.objects.all()
    context ={
        'mobiles': mobile,
        'smarts': smart,
        'Diys': diy,
        'computers': computer
    }
    return render(request, 'deals.html', context)


def laptop(request):
    laptops = Laptops.objects.all()
    appliances = Appliances.objects.all()
    context = {
        'laptops': laptops,
        'appliances': appliances
    }
    return render(request, 'laptops.html', context)


def phones(request):
    trending = Trending.objects.all()
    available = Available.objects.all()
    context ={
        'trending': trending,
        'available': available
    }
    return render(request, 'phones.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        contact = Contact(contact_name=name, contact_email=email, contact_phone=phone, contact_message=message)
        contact.save()
        messages.success(request, 'your message had been submitted successfully')
        return redirect('/contact/')

    return render(request, 'contacts.html')

def cart(request):
    cart = request.session.get("cart", {})  # Get cart from session
    cart_items = []
    total_price = 0
    for product_id, quantity in cart.items():
        try:
            product = get_object_or_404(Product, id=int(product_id))  # Convert ID to int
            cart_items.append({
                "product": product,
                "quantity": quantity,
                "subtotal": product.price * quantity,
            })
            total_price += product.price * quantity
        except:
            print(f"Product ID {product_id} not found in the database.")

    message = "Cart is empty" if not cart_items else None

    return render(request, "cart.html", {
        "cart_items": cart_items,
        "total_price": total_price,
        "message": message,
    })

def add_to_cart(request, product_id):
    cart = request.session.get("cart", {})
    product_id = str(product_id)

    if product_id in cart:
        cart[product_id] += 1
    else:
        cart[product_id] = 1
    request.session["cart"] = cart
    request.session.modified = True

    # Debugging: Print cart to check values
    print("Updated Cart:", request.session["cart"])
    return redirect("cart")


def newsletter_subscriptions(request):
    if request.method == "POST":
        email = request.POST.get('email')
        if email:
            messages.success(request, "Thank you for your subscription!")
            return redirect('index')
    return redirect('index')

def Store(request):
    return render(request, 'store.html')


def search(request):
    query = request.GET.get('search', '')

    category = request.GET.get('category', '')

    results = Product.objects.all()

    if query:
        results = results.filter(name__icontains=query)

    if category and category != "0":
        results = results.filter(category=category)

    print(f"Search Query: {query}")
    print(f"Category: {category}")
    print(f"Results: {results}")

    return render(request, 'results.html', {"results": results, "query": query, "selected_category": category})

def Cart_item(request):
    cart_item =Item.objects.all
    context ={
        'cart_item': cart_item
    }
    return render(request, 'cart.html', context)


def remove_from_cart(request, product_id):
    cart = request.session.get("cart", {})
    product_id = str(product_id)
    if product_id in cart:
        del cart[product_id]
    request.session["cart"] = cart
    return redirect("cart")


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username already taken')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email is taken')
                return redirect('register')

        user = User.objects.create_user(username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name)
        user.save()

        return redirect('win_user')
    else:
       return render(request, 'register.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username,
                            password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid username or password')
            return redirect('login_user')
    else:
        return render(request, 'login.html')

def logout_user(request):
    auth.logout(request)
    return redirect('login_user')


def place_order(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        address = request.POST['address']
        city = request.POST['city']
        country = request.POST['country']
        zipCode = request.POST['zip-code']
        tele = request.POST['tel']
    return render(request, 'checkout.html')



















