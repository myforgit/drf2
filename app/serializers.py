from rest_framework import serializers

from app.models import clases


class claes(serializers.Serializer):
    username = serializers.CharField(max_length=4)
    age = serializers.IntegerField()
    fputs = serializers.IntegerField()
    slat = serializers.SerializerMethodField()
    def get_slat(self,obj):
        return "slat"




class claesde(serializers.Serializer):
    username = serializers.CharField(max_length=4)
    age = serializers.IntegerField()
    fputs = serializers.IntegerField()

    def create(self, validated_data):
        print(validated_data)
        return clases.objects.create(**validated_data)