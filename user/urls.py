from django.urls import include, path
from django.contrib.auth import \
    views as auth_views
from django.contrib.auth.forms import \
    AuthenticationForm
from django.urls import reverse_lazy
from django.views.generic import (
    RedirectView, TemplateView)

from .views import (
    ActivateAccount, CreateAccount,
    DisableAccount, ResendActivationEmail)

password_urls = [
    path('change/',
        auth_views.PasswordChangeView.as_view(
            success_url=reverse_lazy('dj-auth:password_change_done')),
            name='password_change'),
    path('change/done/',
        auth_views.PasswordChangeDoneView.as_view(),
        name='password_change_done'),


    path('reset/',
        auth_views.PasswordResetView.as_view(
        email_template_name='registration/password_reset_email.txt',
        success_url=reverse_lazy('dj-auth:password_reset_done')),
        name='password_reset'),

    path('reset/done/',
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
        success_url=reverse_lazy('dj-auth:password_reset_complete')
        ),
        name='password_reset_confirm'),
    path('done/',
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'),
]

app_name = 'user'
urlpatterns = [
    path('',
        RedirectView.as_view(
            pattern_name='dj-auth:login',
            permanent=False)),
    path('activate/<uidb64>/<token>/',
        ActivateAccount.as_view(),
        name='activate'),
    path('activate/resend/',
        ResendActivationEmail.as_view(),
        name='resend_activation'),
    path('activate/',
        RedirectView.as_view(
            pattern_name=(
                'dj-auth:resend_activation'),
            permanent=False)),
    path('create/',
        CreateAccount.as_view(),
        name='create'),
    path('create/done/',
        TemplateView.as_view(
            template_name=(
                'registration/user_create_done.html')),
        name='create_done'),
    path('disable/',
        DisableAccount.as_view(),
        name='disable'),
    path('login/',
        auth_views.LoginView.as_view(),
        name='login'),
    path('logout/',
        auth_views.LogoutView.as_view(),
        {'extra_context':
             {'form': AuthenticationForm}},
        name='logout'),
    path('password/', include(password_urls)),
]
