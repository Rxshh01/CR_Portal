from django.contrib import admin
from django.conf import settings
# from django.conf.urls.static import static
from django.urls import path,include
from . import views
#from django.views.generic import TemplateView
#from django.contrib.auth.views import LogoutView

urlpatterns = [

    path("",views.smart_home,name='home_view'),
    path("register",views.register_view,name='register_name'),
    path("registered",views.registered,name='registered_name'),
    path("pitch_submission",views.pitch_view,name='pitch_submission'),
    path("pitch_submitted",views.pitch_submitted,name='pitch_submitted'),
#    path("goggle",views.google,name='google_name'),
#   path('', TemplateView.as_view(template_name="google.html")),
#   path('accounts/', include('allauth.urls')),
#   path('logout', LogoutView.as_view()),
]

