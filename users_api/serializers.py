from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField( ## Required for retrieving Users based on Username rather than id
        view_name='user-detail',
        lookup_field='username'
    ) 
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
        
    class Meta:
        model = User
        fields = ['url', 'username', 'password', 'email', 'groups']
