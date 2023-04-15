from django.urls import path
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('token1/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token1/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('token1/verify/', jwt_views.TokenVerifyView.as_view(), name='token_verify'),
]