import re
from django.http import HttpResponseRedirect, FileResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib import messages
from django import forms
from .forms import CustomUserCreationForm, CustomUserChangeForm, ProfileUpdateForm, RegisterForm
from .models import Profile, User
from .helpers import valid_registration
#from random import randint
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        form1 = RegisterForm(request.POST)
        if form.is_valid() and form1.is_valid():
                user = form.save( commit=False )

                #regex = r'[A-Z][0-9]{2,2}'
                user.save()

                profile=Profile(user=user)
                profile.save()
                messages.success(request, f'An account for {user.last_name} {user.first_name} has been created!')
                return redirect('login')
        else:
            context = {'form': form, 'form1':form1 }
            return render(request, 'users/register new.html', context )
    else:

        form = CustomUserCreationForm()
        form1 = RegisterForm()

        context = {'form':form, 'form1':form1 }
        return render(request, 'users/register new.html', context )
        
@login_required
def edit_profile(request):
    title = 'Edit Account'
    if request.method == 'POST':
        u_form = CustomUserChangeForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = CustomUserChangeForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

        context = {
            'u_form': u_form,
            'p_form': p_form,
            'title': title
        }

        return render(request, 'users/profile new.html', context)

def default(request, filename):

    response = FileResponse( open(f'media/{filename}', 'rb') )
    return response
