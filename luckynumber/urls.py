"""
URL configuration for luckynumber project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from useraccounts import views



urlpatterns = [
    path('admin/', admin.site.urls),   
    path('luckynumber-home', views.homepage_view, name='index'),
    path('useraccounts/login/', views.login_view, name='login'),
    path('', views.login_view, name='login'),
    path('useraccounts/signup/', views.signup_view, name='signup'),
    path('pages/lose/', views.lose_view, name='lose'),
    path('win/', views.win_view, name='win'),
    path('withdraw/', views.withdraw_view, name='withdraw'),
    path('wallet/', views.wallet_view, name='wallet'),
    path('deposit/', views.deposit_view, name='deposit'),
    path('processing/', views.processing_view, name='processing'),
    path('referral/', views.referral_view, name='referral')
    
]

