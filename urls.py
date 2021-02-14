from django.urls import path
from . import views as m
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetConfirmView

urlpatterns = [
    # homepage for testing
    path('',m.home, name="home"),
    
    # register and login
    path('register', m.register),
    path('login',m.login, name="login"),

    # authentication
    path(
        'reset_password/',
        auth_views.PasswordResetView.as_view(template_name = "auth_app/reset_password.html"),
        name="reset_password"
    ),
    path(
        'reset_password_sent/',
        auth_views.PasswordResetDoneView.as_view(template_name = "auth_app/reset_password_sent.html"),
        name="password_reset_done"
    ),
    path(
        'reset/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(template_name = "auth_app/change_password.html"),
        name="password_reset_confirm"
    ),
    path(
        'reset_password_complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name = "auth_app/reset_password_complete.html"),
        name="password_reset_complete"
    )
]