from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import ProfileForm, SignupForm, UserForm#, LoginForm
from .models import Profile

# Create your views here.


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username= username, password= password)
            login(request, user)
            return redirect('accounts:profile')
    else:
        form = SignupForm()

    return render(request,'registration/signup.html',{'form':form})





# def login(request):
#     if request.method == "POST":
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')  # Replace 'home' with your desired URL after successful login
#             else:
#                 # Handle invalid login credentials
#                 error_message = "Invalid username or password."
#                 return render(request, 'login.html', {'form': form, 'error_message': error_message})
#     else:
#         form = AuthenticationForm()

#     return render(request, 'login.html', {'form': form})







def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'accounts/profile.html', {'profile': profile})





def profile_edit(request):

    profile = Profile.objects.get(user=request.user)
    if request.method == "POST":
        userform = UserForm(request.POST, instance=request.user)
        profileform = ProfileForm(request.POST,request.FILES, instance=profile)
        if userform.is_valid and profileform.is_valid():
            userform.save()
            myprofile = profileform.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect(reverse('accounts:profile'))
        
    else:
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=profile)

    return render(request, 'accounts/profile_edit.html', {'userform': userform, 'profileform': profileform})
    


def logout(request):
    logout(request)
    return redirect('home')  # Redirect to a specific URL after logout, 'home' in this case








