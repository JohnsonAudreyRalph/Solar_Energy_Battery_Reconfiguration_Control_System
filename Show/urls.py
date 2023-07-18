from django.urls import path
from .views import *

urlpatterns = [
    path('', Login.as_view()),
    path('Login_Success', Affter_Login.as_view(), name='Affter_Login'),
    path('index_HTML', index_HTML, name='index_HTML'),
    path('solars_HTML', solars_HTML, name='solars_HTML'),
    path('configuration_HTML', configuration_HTML, name='configuration_HTML'),
    path('changepass_HTML', changepass_HTML, name='changepass_HTML'),
    path('Logout', Logout, name='Logout')
]