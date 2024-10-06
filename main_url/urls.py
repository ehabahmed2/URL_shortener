from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('u/<str:short_url>/', views.urlRedirect, name='redirect'),
    path("register/", views.register_user, name="register"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
]