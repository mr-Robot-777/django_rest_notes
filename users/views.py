from rest_framework.viewsets import ModelViewSet
# from .models import NoteUser
from .models import User
from .serializers import NoteUserModelSerializer


class NoteUserModelViewSet(ModelViewSet):
    # queryset = NoteUser.objects.all()
    queryset = User.objects.all()
    serializer_class = NoteUserModelSerializer
