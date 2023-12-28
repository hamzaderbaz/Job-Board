from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.contrib import messages
from django.core.mail import send_mail

from .models import Info
from django.conf import settings

def send_message(request):
    myinfo = Info.objects.first()
    
    if request.method == 'POST':
        user_name = request.POST.get('name')
        user_email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        email = EmailMessage(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,  # Set your sending email here
            [settings.DEFAULT_FROM_EMAIL],  # Your email address where you want to receive these messages
            reply_to = [user_email],  # Set the reply-to field to the user's email
        )

        email.from_email = f'{user_name} <{user_email}>'  # Set sender's display name and email
        email.send()
        messages.success(request, 'Your Email Was Sent Successfully!')
        return redirect('contact:contact')
    
    return render(request, 'contact/contact.html', {'myinfo': myinfo})




















# from django.shortcuts import render
# from django.core.mail import EmailMessage
# from django.contrib import messages
# from django.core.mail import send_mail

# from .models import Info
# from django.conf import settings

# def send_message(request):
#     myinfo = Info.objects.first()
    
#     if request.method == 'POST':
#         user_name = request.POST.get('name')
#         user_email = request.POST.get('email')
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')
        
#         send_mail(
#             subject,
#             message,
#             settings.DEFAULT_FROM_EMAIL,  # Set your sending email here
#             [settings.DEFAULT_FROM_EMAIL],  # Your email address where you want to receive these messages
#             reply_to = [user_email],  # Set the reply-to field to the user's email
#         )

#         send_mail.from_email = f'{user_name} <{user_email}>'  # Set sender's display name and email
#         send_mail.send()

#         messages.success(request, 'Your email was sent Successfully!')

#     return render(request, 'contact/contact.html', {'myinfo': myinfo})






# from django.core.mail import send_mail

# send_mail(
#     'Subject here',
#     'Here is the message.',
#     'hamza.derbaz12@gmail.com',  # Sender's email address
#     ['hamza.derbaz@gmail.com'],  # List of recipient(s)
#     fail_silently=False,
# )