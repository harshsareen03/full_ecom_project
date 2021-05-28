from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models.product import Product
from .models.category import Category
from django.views import View
from .models.orders import Order
from django.contrib.auth.models import User
from .models.customer import Customer
from django.contrib.auth.hashers import make_password, check_password


# class Prd(View):
#     def post(self, request):
#
#         product = request.POST.get('product')
#         cart = request.session.get('cart')
#         if cart:
#             quantity = cart.get(product)
#             if quantity:
#                 cart[product] = quantity + 1
#             else:
#                 cart[product] = 1
#
#         else:
#             cart = {}
#             cart[product] = 1
#         request.session['cart'] = cart
#         print('cart', request.session['cart'])
#         return redirect('prd')

# def post(self, request):
#
#     product = request.POST.get('product')
#     cart = request.session.get('cart')
#     if cart:
#         cart[product] = 1
#     else:
#         cart = {}
#         cart[product] = 1
#     request.session['cart'] = cart
#     return redirect('prd')

# def post(self, request):
#     product = request.POST.get('product')
#     print(product)
#     return redirect('prd')


# def get(self, request):
#     products = None
#     categories = Category.get_all_categories()
#     categoryid = request.GET.get('category')
#     if categoryid:
#         products = Product.get_all_products_by_categoryid(categoryid)
#     else:
#         products = Product.get_all_products()
#     data = {}
#     data['products'] = products
#     data['categories'] = categories
#     print(products)
#     return render(request, 'products/productss.html', data)
class Index(View):
    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        print('cart', request.session['cart'])

        return redirect('http://127.0.0.1:8000/products/')

    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        products = None
        categories = Category.get_all_categories()
        categoryid = request.GET.get('category')
        if categoryid:
            products = Product.get_all_products_by_categoryid(categoryid)
        else:
            products = Product.get_all_products()
        data = {'products': products, 'categories': categories}

        return render(request, 'products/productss.html', data)


class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        print(products)
        return render(request, 'products/cart.html', {'products': products})


class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        print(address, phone, customer, cart, products)

        for product in products:
            print(cart.get(str(product.id)))
            order = Order(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)))
            order.save()
        request.session['cart'] = {}

        return redirect('cart')


class OrderView(View):

    def get(self, request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        return render(request, 'products/orders.html', {'orders': orders})


class Signup(View):
    def get(self, request):
        return render(request, 'registration.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        error_message = None

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)
        error_message = self.validateCustomer(customer)

        if not error_message:
            print(first_name, last_name, phone, email, password)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('index')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'registration.html', data)

    def validateCustomer(self, customer):
        error_message = None;
        if (not customer.first_name):
            error_message = "First Name Required !!"
        elif len(customer.first_name) < 4:
            error_message = 'First Name must be 4 char long or more'
        elif not customer.last_name:
            error_message = 'Last Name Required'
        elif len(customer.last_name) < 4:
            error_message = 'Last Name must be 4 char long or more'
        elif not customer.phone:
            error_message = 'Phone Number required'
        elif len(customer.phone) < 10:
            error_message = 'Phone Number must be 10 char Long'
        elif len(customer.password) < 6:
            error_message = 'Password must be 6 char long'
        elif len(customer.email) < 5:
            error_message = 'Email must be 5 char long'
        elif customer.isExists():
            error_message = 'Email Address Already Registered..'
        # saving

        return error_message


class Login(View):
    return_url = None

    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id

                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('product')
            else:
                error_message = 'Email or Password invalid !!'
        else:
            error_message = 'Email or Password invalid !!'

        print(email, password)
        return render(request, 'products/productss.html', {'error': error_message})
