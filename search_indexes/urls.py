from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .viewsets.book import BookDocumentView


router = DefaultRouter()
books = router.register(r'books',
                        BookDocumentView,
                        basename='bookdocument')


urlpatterns = [
    path('', include(router.urls)),
]
