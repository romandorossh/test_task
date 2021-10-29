from rest_framework import serializers
from lang_detector.models import Snippet
from lang_detector.textual_service import TextualService


class SnippetSerializer(serializers.ModelSerializer):
    id = serializers.CharField()

    class Meta:
        model = Snippet
        fields = ['id', 'text', 'language']

    def create(self, validated_data):
        _id = validated_data.get("id")
        text = validated_data.get("text")

        ts = TextualService()
        instance = ts.add(_id, text)

        return instance

    def update(self, instance, validated_data):
        ts = TextualService()
        instance = ts.update(instance, validated_data)
        return instance
