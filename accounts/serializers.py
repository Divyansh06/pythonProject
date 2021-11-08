from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('is_active', 'is_staff', 'is_superuser')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'min_length': 4
            }
        }
