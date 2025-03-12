"""
URL configuration for mycompany project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# from myapp import views 
from account import views as acc_views
from Hr import views as hr_views

urlpatterns = [
    path('', hr_views.welcomeHr, name='hrr'), # هنا نضيف الراب
    # path('', views.Home, name='home'), # هنا نضيف الرابط للدالة
    path('admin/', admin.site.urls),
    # path('message/', views.Message, name='message'), # هنا نضيف الرابط للدالة
    # path('name/<str:name>/', acc_views.accoHello), # هنا نضيف الرابط للدالة
    path('add/<int:num1>/<int:num2>/', acc_views.addtwo), 
    path('acc/', acc_views.index, name='acc'),
    path('about/', acc_views.about, name='about'),
]


# كل دالة نحطها في الفيو نضمن رابطها اهنا