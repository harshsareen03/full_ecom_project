from django.urls import path
from . import views
from .views import Index, Cart, CheckOut, OrderView, Signup, Login

urlpatterns = [
    # path('prd/', views.prd, name='prd'),
    path('', Index.as_view(), name='product'),
    path('cart/', Cart.as_view(), name='cart'),
    path('checkout/', CheckOut.as_view(), name='checkout'),
    path('order/', OrderView.as_view(), name='order'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
]
