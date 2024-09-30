from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm
from .models import UserInput

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()
            login(request, user)  # Log in the user after registration
            return redirect('input_text')  # Redirect to the text input page
    else:
        form = UserRegistrationForm()
    return render(request, 'app/register.html', {'form': form})

def input_text(request):
    if request.method == 'POST':
        text_input = request.POST.get('text_input')
        # Create an instance of your UserInput model to save the data
        UserInput.objects.create(user=request.user, text=text_input)
        # Optionally redirect or render a success message
        return render(request, 'app/input_text.html', {'success': True})

    return render(request, 'app/input_text.html')