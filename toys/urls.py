from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ToyViewSet

router = DefaultRouter()
router.register(r'toys', ToyViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('toys/update_by_name/<str:name>/', ToyViewSet.as_view({'put': 'update_by_name'}), name='toy-update-by-name'),
    path('toys/delete_by_name/<str:name>/', ToyViewSet.as_view({'delete': 'delete_by_name'}), name='toy-delete-by-name'),
]
