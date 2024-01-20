from django.urls import path
from django.conf.urls import include
from accounts.views import GoogleLoginView


urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('', include('dj_rest_auth.registration.urls')),

    # path('', include('allauth.urls')),
    path('google/login', GoogleLoginView.as_view(), name='api_accounts_google_oauth'),
]
