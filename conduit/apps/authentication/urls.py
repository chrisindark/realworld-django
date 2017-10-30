from django.conf.urls import url

from .views import (
    LoginAPIView, UserCreateRetrieveUpdateAPIView
)

urlpatterns = [
    url(r'^users/?$', UserCreateRetrieveUpdateAPIView.as_view()),
    url(r'^users/login/?$', LoginAPIView.as_view()),
]
