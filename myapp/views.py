from django.shortcuts import redirect, render
from .forms import SignupForm,NotesForm,ContactForm
from .models import user_signup
from django.contrib.auth import logout
from django.core.mail import send_mail
from BatchProject import settings
import requests
import random

# Create your views here.

def index(request):
    if request.method=="POST": #root
        if request.POST.get("signup")=="signup":
            newuser=SignupForm(request.POST)
            if newuser.is_valid():
                newuser.save()
                print("User created successfully!")

                # Send Welcome MAIL!
                sub="Welcome!"
                msg=f"Dear User!\nYour account has been created with us!\nEnjoy our services.\nIf, require any query or help, \nPlease contact on\n+91 9724799469 | sanket@tops-int.com"
                from_ID=settings.EMAIL_HOST_USER
                #to_ID=["ishitpancholi7@gmail.com","mehtamahek221@gmail.com"]
                to_ID=[request.POST['email']]
                send_mail(subject=sub,message=msg,from_email=from_ID,recipient_list=to_ID)
                print("Email send successfully!")
                return redirect("notes")
            else:
                print(newuser.errors)
        elif request.POST.get("login")=="login":

            unm=request.POST["email"]
            pas=request.POST["password"]

            user=user_signup.objects.filter(email=unm,password=pas)
            userid=user_signup.objects.get(email=unm)
            print("UserID:",userid.id)
            if user:
                print("Login Successfull!")

                # Send OTP SMS
                url = "https://www.fast2sms.com/dev/bulkV2"
                otp=random.randint(1111,9999)
                querystring = {"authorization":"PSqGhvu5BkQv1WEvvWH6PIgV0vr1IcOIEzgsN1fZMHFG0WJapJ1hGGIwYfq8","variables_values":f"{otp}","route":"otp","numbers":"7016956121,8849408876"}
                headers = {
                    'cache-control': "no-cache"
                }
                response = requests.request("GET", url, headers=headers, params=querystring)
                print(response.text)

                request.session["user"]=unm
                request.session["userid"]=userid.id
                return redirect("notes")
            else:
                print("Error...Login faild!")
    return render(request,'index.html')

def notes(request):
    user=request.session.get("user")
    if request.method=="POST":
        mynote=NotesForm(request.POST,request.FILES)
        if mynote.is_valid():
            mynote.save()
            print("Your post has been uploaded")
        else:
            print(mynote.errors)
    return render(request,'notes.html',{'user':user})

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method=='POST':
        contctfrm=ContactForm(request.POST)
        if contctfrm.is_valid():
            contctfrm.save()
            print("Your message has ben sent succesfully!")
        else:
            print(contctfrm.errors)
    return render(request,'contact.html')

def userlogout(request):
    logout(request)
    return redirect("/")

def updateprofile(request):
    user=request.session.get("user")
    userid=request.session.get("userid")
    uid=user_signup.objects.get(id=userid)
    if request.method=="POST":
        updateUser=SignupForm(request.POST)
        if updateUser.is_valid():
            updateUser=SignupForm(request.POST,instance=uid)
            updateUser.save()
            print("Your profile has been updated!")
        else:
            print(updateUser.errors)
    return render(request,'updateprofile.html',{'user':user,'cuser':user_signup.objects.get(id=userid)})