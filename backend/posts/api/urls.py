from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

user_router = DefaultRouter()
user_router.register(r'contacts',UserViewSet)

urlpatterns = [
    path('contacts/<int:pk>/update_contact/', UserViewSet.as_view({'put': 'update_contact'}), name='update-contact'),
    path('contacts/<int:pk>/delete_contact/', UserViewSet.as_view({'delete': 'delete_contact'}), name='delete-contact'),
]
