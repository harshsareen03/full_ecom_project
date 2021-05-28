from django.urls import path
from . import views


urlpatterns = [


    path('user_logout/', views.user_logout, name='user_logout'),

    path('contact_m/', views.contact_m, name='contact_m'),
]
