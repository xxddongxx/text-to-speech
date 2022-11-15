from rest_framework import serializers

from tts.models import Project, Audio, Title


class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = "__all__"

class AudioUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = ['text',  'speed']