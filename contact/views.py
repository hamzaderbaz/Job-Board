from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .models import Info

# Create your views here.

def send_message(request):
    myinfo = Info.objects.first()
    
    if request.method =='POST':
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']
        
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [email],
        )
        
    return render(request, 'contact/contact.html',{'myinfo': myinfo})



# from django.conf import settings
# from django.core.mail import send_mail
# from django.shortcuts import render
# from django.http import HttpResponseRedirect

# from .models import Info

# def send_message(request):
#     myinfo = Info.objects.first()
    
#     if request.method == 'POST':
#         subject = request.POST.get('subject')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
        
#         if subject and email and message:
#             try:
#                 send_mail(
#                     subject,
#                     message,
#                     settings.EMAIL_HOST_USER,
#                     [email],
#                 )
#                 # Provide feedback to the user about successful email sending
#                 return render(request, 'contact/success.html', {'myinfo': myinfo})
#             except Exception as e:
#                 # Handle exceptions and provide appropriate feedback to the user
#                 error_message = f"An error occurred: {e}"
#                 return render(request, 'contact/error.html', {'error_message': error_message})
#         else:
#             # Handle case where required fields are missing
#             error_message = "All fields are required."
#             return render(request, 'contact/contact.html', {'myinfo': myinfo, 'error_message': error_message})
    
#     return render(request, 'contact/contact.html', {'myinfo': myinfo})
