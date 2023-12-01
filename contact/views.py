from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages

from .models import Info

def send_message(request):
    myinfo = Info.objects.first()
    
    if request.method == 'POST':
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [email],
        )

        messages.success(request, 'Your email was sent Successfully!')

    return render(request, 'contact/contact.html', {'myinfo': myinfo})