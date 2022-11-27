from django.shortcuts import render,redirect
from .models import Users_data, Users_data
from django.contrib import messages
from django.contrib.auth import authenticate,login as log
from django.core.mail import send_mail

# from django.core.email import send_mail
# from cryptography.fernet import Fernet
# from cryptography.fernet import Fernet
# import base64
# import logging
# import traceback
# from django.conf import settings
# from Crypto.Cipher import AES
# from Crypto.Random import get_random_bytes

# Create your views here.


def signup(request):
    if request.method == 'POST':
        username=request.POST.get('username'),
        name=request.POST.get('name'),
        number=request.POST.get('number'),
        email=request.POST.get('email'),
        password=request.POST.get('password'),
        cpassword=request.POST.get('cpassword'),
        print(username, name, number, email, password,cpassword)

        if username and name and number and email and password : # this will check any filed is not null 
            save_record=Users_data()                # I crete var to save data 
            save_record.username=username[0]           # noe i save data from fileds 
            save_record.name=name[0]                # here i took data in tuple and store only first valur to avoid storening muktipple value in one filed 
            save_record.email=email[0]
            save_record.number=number[0]
            save_record.password=password[0]
            save_record.save()
            messages.success(request,"Yup Record was saved successfully")
            send_mail("test email", "hello"+name[0]+"\n Welcome to Krunal's Would \n you succesfully registerd your account \n your user id is "+username[0]+"", 'project.krunalrana@gmail.com', [email[0]])
            return redirect("login")
        else:
            return render(request,'signup.html')

    return render(request,'signup.html')



def login(request):

    if request.method == "POST":
        username =request.POST.get('username'),
        password=request.POST.get('password'),
        print(username,password)
        print(type(username))

        userdata=Users_data.objects.values('username').all()
        pwd=Users_data.objects.values('username','password','email','name','id').all()
        print(userdata)
        print(pwd)
        b=dict()
        for i in pwd:
            if i['username']== username[0]:
                print(i)
                print(i['password'])
                if i['password']== password[0]:
                    print("yup we got op ")
                    email=i['email']
                    name=i['name']
                    id=i['id'] 
                    # email
                    send_mail("test email", "Hello,"+name+"\n You are succesfully registerd in you account\n Your Registerd id is"+str(id)+"\n thank you for joing us", 'project.krunalrana@gmail.com', [email])
                    return redirect("home")
    return render(request,'login.html')

def home(request):

    return render(request,'home.html')