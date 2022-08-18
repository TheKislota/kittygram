# urls.py
from rest_framework.routers import SimpleRouter

from django.urls import include, path

from cats.views import CatViewSet

router = SimpleRouter()

router.register('cats', CatViewSet)

urlpaterns = [
   path('', include(router.urls)),
]
