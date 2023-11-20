from rest_framework import generics
from .models import Course
from .serializers import CourseSerializer

class CourseList(generics.ListAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        queryset = Course.objects.all()

        rating = self.request.query_params.get('rating', None)
        if rating is not None:
            queryset = queryset.filter(rating__gte=float(rating))

        level = self.request.query_params.get('level', None)
        if level is not None:
            queryset = queryset.filter(level=level)

        language = self.request.query_params.get('language', None)
        if language is not None:
            queryset = queryset.filter(language=language)

        return queryset