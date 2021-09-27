from rest_framework.serializers import HyperlinkedModelSerializer
# from .models import NoteUser
from .models import User


class UserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        # model = NoteUser
        #  fields = ('username', 'firstname', 'lastname', 'email')
        # fields = '__all__'
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        # fields = '__all__'
