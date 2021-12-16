"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# from django.conf.urls import handler400
from django.contrib import admin
from django.urls import path,include
# from myWebsite import views
# from django.conf.urls.static import static
# from django.conf import settings
from django.conf.urls import handler404




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('myWebsite.urls')),
    # path('', views.index),
#     # path('index/<slug:fname>/<slug:lname>/<slug:age>/<slug:hobby>', views.index),
#     path('showName/<slug:fname>/<slug:lname>', views.showName),
#     path('addNews/', views.addNews),
#     # path('resultPage/',views.resultPage, name="resultPage"),
#     path('recordNews/',views.recordNews, name="recordNews"),
#     path('contentNews/',views.contentNews),
#     path('contentEdit/',views.contentEdit, name="contentEdit"),
#     path('contentUpdate/',views.contentUpdate, name ="contentUpdate"),
#     path('contentDelete/',views.contentDelete, name ="contentDelete"),
#     path('contentShow/', views.contentShow, name="contentShow"),
#     path('registUser/', views.registUser),
#     path('registData/', views.registData, name="registData"),
#     path('loginUser/', views.loginUser),
#     path('loginData/', views.loginData, name="loginData"),
#     path('logoutUser/',views.logoutUser),
#     path('loginWarning',views.loginWarning)
    
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
]
handler404 = 'myWebsite.views.handler404'