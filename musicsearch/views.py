from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Song
from .serializers import SongSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search_song(request):
    query = request.query_params.get('name', None)
    genre = request.query_params.get('genre', None)
    year = request.query_params.get('year', None)

    songs = Song.objects.filter(name__icontains=query)

    if genre:
        songs = songs.filter(genres__contains=[genre])

    if year:
        songs = songs.filter(year_release_date=year)

    songs = songs.order_by('name')
    serializer = SongSerializer(songs, many=True)

    return Response(serializer.data)
