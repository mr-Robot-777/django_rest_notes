from rest_framework.viewsets import ModelViewSet
# from .models import NoteUser
from .models import User
from .serializers import UserModelSerializer


class UserModelViewSet(ModelViewSet):
    # queryset = NoteUser.objects.all()
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
