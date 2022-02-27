from django.conf.urls.static import static
from django.urls import re_path
from django.conf import settings

from base import views

urlpatterns = [
    re_path(r'^user$', views.user_view),
    re_path(r'^user/([0-9]+)$', views.user_view),
]