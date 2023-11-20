from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()

        level = self.request.query_params.get('level', None)
        if level is not None:
            queryset = queryset.filter(level=level)

        language = self.request.query_params.get('language', None)
        if language is not None:
            queryset = queryset.filter(language=language)

        rating = self.request.query_params.get('rating', None)
        if rating is not None:
            queryset = queryset.filter(rating__gte=float(rating))

        return queryset