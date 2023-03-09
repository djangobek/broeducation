from django.urls import path
from .views import *

urlpatterns = [
    path('', Mainopen.as_view(), name='maindir'),
    path("pupil_results/", Table.as_view(), name="mianexammet"),
    path("registration/", blog_post, name='registration')
]