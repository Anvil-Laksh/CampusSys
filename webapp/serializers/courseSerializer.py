from rest_framework import serializers

from webapp.models.courses import CoursesModel


class CoursesModelSerialize(serializers.ModelSerializer):
    class Meta:
        model = CoursesModel
        fields = '__all__'
