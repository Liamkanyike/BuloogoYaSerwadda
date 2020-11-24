from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm, UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

def register(request):
	form = UserRegisterForm()


	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, f'Your account has been Created! You are now able to login!')
			return redirect('login')
			
	context = {'form': form}
	return render(request, 'users/register.html', context)


def login_view(request):
	next = request.GET.get('next')
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user = authenticate(username=username, password=password)
		login(request, user)
		if next:
			return('/')

	context = {
		'form': form,
	}
	return render(request, "login.html", context)



@login_required
def profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your account has been updated!')
			return redirect('profile')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)
	

	context = {
		'u_form': u_form,
		'p_form': p_form
	}
	return render(request, 'users/profile.html', context)

