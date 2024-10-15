"""aakar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import redirect_view1 
from . import views
urlpatterns = [
    path('cr/', include('aakarapp.urls')),
    path('accounts/', include('allauth.urls')), 
    path("smartpitch/",include('fnb_app.urls')),


    path("admin/", admin.site.urls),
    path('', redirect_view1),
    path('civifest', views.city_view,name="city_name"),
    path('form', views.form_view,name="form_name"),
    path('task1',views.for_task1,name="task1_error"),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 


