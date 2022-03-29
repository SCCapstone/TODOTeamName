from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'account'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html', extra_context={'login_page': 'active'}), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html', extra_context={'logout_page': 'active'}), name='logout'),
]
