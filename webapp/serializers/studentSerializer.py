from rest_framework import serializers

from webapp.models.Student import StudentModel


class StudentModelSerialize(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = '__all__'
