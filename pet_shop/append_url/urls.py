from django.urls import path, include
from rest_framework.routers import DefaultRouter

from pets import views as pet
from users import views as user
from orders import views as order

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r'pets', pet.PetViewSet, basename='pet')
router.register(r'users', user.UserViewSet, basename='user')
router.register(r'orders', order.OrderViewSet, basename='order')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]