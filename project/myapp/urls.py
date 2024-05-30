from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('quiz/', views.quiz, name='quiz'),
    path('finish/', views.finish, name='finish'),
    path('fail/', views.fail, name='fail'),
    path('raffle/', views.raffle, name='raffle'),
    path('timedout/', views.timedout, name='timedout'),
    path('start-quiz/', views.start_quiz, name='start_quiz'),
    path('login/', LoginView.as_view(template_name='pages/login.html'), name='login')
]