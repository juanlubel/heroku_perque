from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token
from .views import RegistrationUserApi


urlpatterns = [
    url(r'^login$', obtain_jwt_token, name='get-token'),
    url(r'^register', RegistrationUserApi.as_view(), name='set-token'),
    url(r'^user', verify_jwt_token, name='set-token'),
]
