from rest_framework import serializers
from core.models import Server, Lab, User, Complain, Command


class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Server
        fields = (
            'id',
            'Hostname',
            'IPAddress',
            'OS',
            'Lastcommand',
            'output',
            'runcommand',
            'lab',
            'status',
            'timestamp'
        )
        read_only_fields = ['id']


class LabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lab
        fields = (
            'id',
            'labname',

        )
        read_only_fields = ['id']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'user_name',
            'password',
            'os'

        )
        read_only_fields = ['id']


class ComplainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complain
        fields = (
            'id',
            'firstname',
            'lastname',
            'subject'

        )
        read_only_fields = ['id']


class CommandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Command
        fields = (
            'id',
            'commandname',
            'os',

        )
        read_only_fields = ['id']
