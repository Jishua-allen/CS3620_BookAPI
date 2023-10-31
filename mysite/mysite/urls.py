"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from BookAPI.views import BookViewSet, FantasyBookViewSet, SciFiBookViewSet, MysteryBookViewSet, LitRPGBookViewSet, HorrorBookViewSet, RomanceBookViewSet, FavoritesBookViewSet, TopRatedBookViewSet, NonFictionBookViewSet, ThrillerBookViewSet

router = routers.SimpleRouter()
router.register('books', BookViewSet)
router.register('fantasy', FantasyBookViewSet)
router.register('scifi', SciFiBookViewSet)
router.register('mystery', MysteryBookViewSet)
router.register('litrpg', LitRPGBookViewSet)
router.register('horror', HorrorBookViewSet)
router.register('romance', RomanceBookViewSet)
router.register('favorites', FavoritesBookViewSet)
router.register('toprated', TopRatedBookViewSet)
router.register('nonfiction', NonFictionBookViewSet)
router.register('thriller', ThrillerBookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
