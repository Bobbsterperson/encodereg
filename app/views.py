import base64
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm
from .models import UserInput
from django.contrib.auth import authenticate, login
from .forms import UserLoginForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('input_text')
    else:
        form = UserRegistrationForm()
    return render(request, 'app/register.html', {'form': form})

def input_text(request):
    if request.method == 'POST':
        text_input = request.POST.get('text_input')
        encoded_text = base64.b64encode(text_input.encode('utf-8')).decode('utf-8')
        UserInput.objects.create(user=request.user, text=encoded_text)
        return render(request, 'app/input_text.html', {'success': True, 'encoded_text': encoded_text})
    return render(request, 'app/input_text.html')

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('input_text') 
            else:
                return render(request, 'app/login.html', {'form': form, 'error': 'Invalid username or password'})
    else:
        form = UserLoginForm()
    return render(request, 'app/login.html', {'form': form})
