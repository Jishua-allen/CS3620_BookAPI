import requests
from django.core.management.base import BaseCommand
from ...models import Book

def getBooks():
    url = 'https://api.nytimes.com/svc/books/v3/lists/current/hardcover-fiction.json?api-key=1H5B6jQK4Xr3bG7JGJmG2e0V0X7y7q2E'
    response = requests.get(url)
    data = response.json()
    books = data['results']['books']
    return books