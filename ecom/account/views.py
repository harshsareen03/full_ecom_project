import smtplib

from django.conf import settings
from django.contrib import messages, auth
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse

from .forms import UserForm
from django.contrib.auth import authenticate, login, logout

from django.http import HttpResponseRedirect
from django.core.mail import send_mail
import email.message
from django.contrib.auth.hashers import make_password

from django.views import View
from django.contrib.auth.hashers import check_password


#
# def register(request):
#     registered = False
#     if request.method == 'POST':
#         user_form = UserForm(data=request.POST)
#
#         if user_form.is_valid():
#             user = user_form.save()
#             user.set_password(user.password)
#             user.save()
#
#             registered = True
#         else:
#             print(user_form.errors)
#     else:
#         user_form = UserForm()
#
#     return render(request, 'registration.html',
#                   {'user_form': user_form,
#
#                    'registered': registered})


def user_logout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect("http://127.0.0.1:8000/")


def contact_m(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        data_content = [subject, name]
        send_mail(data_content, message, settings.EMAIL_HOST_USER, [email], fail_silently=False)
    else:
        print('i dont get it')
    return render(request, 'contact/contact.html')
