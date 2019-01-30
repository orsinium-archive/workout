# external
from django.urls import include, path
from rest_framework_jwt import views as jwt

# app
from .api import router


urlpatterns = [
    path(r'token/obtain/',    jwt.ObtainJSONWebToken.as_view(), name='jwt_obtain'),
    path(r'token/verify/',    jwt.VerifyJSONWebToken.as_view(), name='jwt_verify'),
    path(r'token/refresh/',   jwt.RefreshJSONWebToken.as_view(), name='jwt_refresh'),

    path('', include(router.urls)),
]
