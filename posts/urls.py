
from django.urls import path

from .views import *

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', log_in, name='login'),
    path('logout/', log_out, name='logout'),
    path('profile/<username>/', profile, name='profile'),
    path('edit-profile/', edit_profile, name='edit_profile'),
    path('api/v1/profiles/', profileList, name='profiles'),
]

