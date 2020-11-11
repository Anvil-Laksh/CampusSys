from rest_framework import serializers

from webapp.models.faculty import FacultyModel


class FacultyModelSerialize(serializers.ModelSerializer):
    class Meta:
        model = FacultyModel
        fields = '__all__'
