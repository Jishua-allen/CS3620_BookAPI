from django.shortcuts import render
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer


# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class FantasyBookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.filter(category='Fantasy')
    serializer_class = BookSerializer

class SciFiBookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.filter(category='Sci-Fi')
    serializer_class = BookSerializer

class MysteryBookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.filter(category='Mystery')
    serializer_class = BookSerializer

class LitRPGBookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.filter(category='LitRPG')
    serializer_class = BookSerializer

class HorrorBookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.filter(category='Horror')
    serializer_class = BookSerializer

class RomanceBookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.filter(category='Romance')
    serializer_class = BookSerializer

class FavoritesBookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.filter(category='Favorites')
    serializer_class = BookSerializer

class TopRatedBookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.order_by('-rating')
    serializer_class = BookSerializer

class NonFictionBookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.filter(category='Non-Fiction')
    serializer_class = BookSerializer

class ThrillerBookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.filter(category='Thriller')
    serializer_class = BookSerializer
    

