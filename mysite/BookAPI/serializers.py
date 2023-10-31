from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
  image = serializers.ImageField(max_length=None, use_url=True)
  class Meta:
    model = Book
    fields = ('id', 'title', 'description', 'category', 'rating', 'image')