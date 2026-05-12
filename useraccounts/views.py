from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        #checking if eamil already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered.')
            return redirect('signup')
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, 'Account created successfully!')
        return redirect('login')

    return render(request, 'signup.html')
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
           
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid Credentials')
    return render(request, 'login.html')

def homepage_view(request):
    return render(request, 'index.html')
def lose_view(request):
    return render(request, 'lose.html')
def win_view(request):
    return render(request, 'win.html')
def withdraw_view(request):
    return render(request, 'withdraw.html')
def wallet_view(request):
    return render(request, 'wallet.html')
def deposit_view(request):
    # if request.method == 'POST':
    #     amount = request.POST['amount']
    #     amount.save()
    #     messages.success(request, "Thank you for depositing")
    return render(request, 'deposit.html')
def processing_view(request):
    return render(request, 'processing.html')
def referral_view(request):
    return render(request, 'referral.html')
