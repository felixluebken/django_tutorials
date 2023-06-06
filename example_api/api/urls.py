from django.urls import re_path,include

from .views import *


urlpatterns = [
    re_path(r'^', HelloView.as_view())
]