from rest_framework.serializers import ModelSerializer #HyperlinkedModelSerializer
from rest_framework import serializers
from .models import Project, Todo
from users.serializers import UserModelSerializer

class ProjectModelSerializer(ModelSerializer):
    # users = serializers.StringRelatedField(many=True) # закомитил для дз 11

    class Meta:
        model = Project
        fields = ('id', 'url', 'name', 'repository', 'users')
        # fields = ('name', 'repository', 'users')


class ProjectModelSerializerShort(ModelSerializer):
    users = serializers.StringRelatedField(many=True)
    users = UserModelSerializer(many=True)

    class Meta:
        model = Project
        # fields = '__all__'
        fields = ('id', 'url', 'name', 'users')


class TodoModelSerializer(ModelSerializer):
    # user = UserModelSerializer() # закомитил для дз 11
    # project = ProjectModelSerializer() # закомитил для дз 11

    class Meta:
        model = Todo
        fields = ('id', 'url', 'project', 'text', 'created', 'updated', 'user', 'is_active')
        # fields = ('project', 'text', 'created', 'updated', 'user', 'is_active')
