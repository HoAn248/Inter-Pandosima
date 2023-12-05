
from django.urls import path,include
from append_url import urls
urlpatterns = [
    path('', include(urls)),
]
