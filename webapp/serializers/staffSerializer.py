from rest_framework import serializers

from webapp.models.staff import StaffModel


class StaffModelSerialize(serializers.ModelSerializer):
    class Meta:
        model = StaffModel
        fields = '__all__'
