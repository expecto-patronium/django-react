from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views

urlpatterns = [
    # path('hello/', views.HelloView.as_view(), name='hello'),
    path('test/', views.test_api, name='test'),
    path('api/', include('rest_framework.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.register_user, name='register'),
    path('add-todo/', views.add_todo, name='add-todo'),
    path('get-todo/<int:pk>', views.get_todo, name='get-todo'),
    path('update-todo/<int:pk>/', views.update_todo, name='update-todo'),
    path('all-todo/', views.all_todo, name='all-todo'),
    path('delete-todo/<int:pk>/', views.delete_todo, name='all-todo'),
    path('profile/', views.UserprofileView.as_view()),
    path('', TemplateView.as_view(template_name='index.html')),
    path('login/', TemplateView.as_view(template_name='index.html')),
    path('home/', TemplateView.as_view(template_name='index.html')),
    path("google_user/", views.get_google_user),
    path("hello/", views.hello)
]
