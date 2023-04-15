from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api import views

urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('test/', views.test_api, name='test'),
    path('api/', include('rest_framework.urls')),
    path('', include('todo_app.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh')
]