from django.urls import path,include
from . import views

from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from .views import redirect_view



urlpatterns = [
    path('', views.home, name="home"),
    path('accounts/', include('allauth.urls')),
    path('dashboard', views.dashboard, name="dashboard"),
    path('updateProfile', views.updateProfile, name="updateProfile"),
    path('task1',views.task1,name="task1"),
    path('task2',views.task2,name="task2"),
    path('task3',views.task3,name="task3"),
    path('task4',views.task4,name="task4"),
   path('task5',views.task5,name="task5"),
     path('task6',views.task6,name="task6"),
     path('task7',views.task7,name="task7"),
 path('task8',views.task8,name="task8"),
    path('competition',views.compi_home,name='light_theme'),
    path('aakaar_new',views.aakaar_new,name='aakaar_new'),
    path('email_submitted',views.email_submission,name='email_urlname'),
    path('email_in',views.email_in,name='email old'),
     path('time',views.time_view,name='time '),
   path('tally',views.tally_view,name='tally '),
path('scores',views.scorecard_view,name='scorecard '),
path('team',views.team_view,name="team_name"),
path('logiq',views.logiq,name='logiq'),
path('leaderboard',views.leaderboard, name='leaderboard')




]
