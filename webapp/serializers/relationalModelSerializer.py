from rest_framework import serializers

from webapp.models.relationModel import StudentParentRelation, StudentFacultyCourses


class StudentParentRelationSerialize(serializers.ModelSerializer):
    class Meta:
        model = StudentParentRelation
        fields = '__all__'


class StudentFacultyCoursesSerialize(serializers.ModelSerializer):
    class Meta:
        model = StudentFacultyCourses
        fields = '__all__'

