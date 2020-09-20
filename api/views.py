from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import MovieSerializer, MovieMiniSerializer
from .models import Movie
from rest_framework.response import Response

class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def list(self, request, *args, **kwargs):
        movies = Movie.objects.all()
        serializers = MovieMiniSerializer(movies, many=True)
        return Response(serializers.data)