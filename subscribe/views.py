# from typing_extensions import final
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

from .forms import Subscribe

s = Subscribe()
print(s)

print("Hello")

# from myproject.settings import EMAIL_HOST_USER
from django.conf import settings
from django.core.mail import message, send_mail,EmailMessage

# Create your views here.
#DataFlair #Send Email
def subscribe_email(request):
    print("In subscribe_mail")
    sub = Subscribe()
    # print(sub)
    # return HttpResponse("Hi..")

    if request.method == 'POST':
        sub = Subscribe(request.POST)    #email
        subject1 = 'Welcome to DataFlair'
        message1 = 'Hope you are enjoying your Django Tutorials'
        recepient = request.POST["email"].strip()
        print(recepient)
        final_rec_list = None
        if ";" in recepient:
            final_rec_list = recepient.split(";")
        else:
            final_rec_list = [recepient]
        print(final_rec_list,"final_rec_list")
        if final_rec_list:
            msg = EmailMessage(subject=subject1,body=message1,from_email=settings.EMAIL_HOST_USER,to= final_rec_list)
            send_mail(subject = subject1,message=message1,from_email=settings.EMAIL_HOST_USER,recipient_list=final_rec_list)
            msg.attach_file("D:\\MyPython\\MySQL\\sql_first.py")
            msg.send(fail_silently=False)
        return render(request,'success.html', {'recepient': recepient})
    # return render(request, 'subscribe/index.html', {'form':sub})
    return render(request,'index.html',context={'form1':sub})


    # if request.method == 'POST':
    #     sub = Subscribe(request.POST)
    #     subject = 'Welcome to DataFlair'
    #     message = 'Hope you are enjoying your Django Tutorials'
    #     recepient = str(sub['Email'].value())
    #     send_mail(subject, 
    #         message, settings.EMAIL_HOST_USER, [recepient], fail_silently = False)
    #     return render(request, 'subscribe/success.html', {'recepient': recepient})
    # return render(request, 'subscribe/index.html', {'form':sub})