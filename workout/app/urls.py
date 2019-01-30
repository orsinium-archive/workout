from rest_framework_jwt import views as jwt

from django.urls import include, path

from .api import router


urlpatterns = [
    path(r'token/obtain',    jwt.ObtainJSONWebToken.as_view()),
    path(r'token/verify',    jwt.VerifyJSONWebToken.as_view()),
    path(r'token/refresh',   jwt.RefreshJSONWebToken.as_view()),

    path('', include(router.urls)),
]
