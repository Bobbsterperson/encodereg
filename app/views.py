import base64
import hashlib
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm, UserLoginForm
from .models import UserInput, UserProfile


class Encoder:
    def encode(self, text):
        pass

class Base64Encoder(Encoder):
    def encode(self, text):
        return base64.b64encode(text.encode()).decode()

class HashEncoder(Encoder):
    def encode(self, text):
        return hashlib.sha256(text.encode()).hexdigest()
    
def encrypt_text(text, encoder):
    return encoder.encode(text)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            UserProfile.objects.create(user=user, encoding_method='base64')
            login(request, user)
            return redirect('input_text')
    else:
        form = UserRegistrationForm()
    return render(request, 'app/register.html', {'form': form})

def input_text(request):
    if request.method == 'POST':
        text_input = request.POST.get('text_input')
        encoding_method = request.user.userprofile.encoding_method
        encoder = Base64Encoder() if encoding_method == 'base64' else HashEncoder()
        encoded_text = encrypt_text(text_input, encoder)
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

