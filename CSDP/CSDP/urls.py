"""CSDP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path,include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from main.views import redirectView
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url
from django.contrib.auth import views as auth_views



urlpatterns = [

    #stands for loginpage
url(r'^', include('login.urls')),
path('admin/', admin.site.urls),

    # stands for homepage
    path('welcome/', include('main.urls')),
    # regx will say for whom it's been made :p
    path('',redirectView),
    path('teachers/', include('teachers.urls')),
    path('students/',include('students.urls',namespace='student')),
]
admin.site.site_header="Aravali CSDP Admin Login"
admin.site.site_title="Computer Science Department Portal"
admin.site.index_title="Welcome to Aravali Computer Science Department Portal"

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)