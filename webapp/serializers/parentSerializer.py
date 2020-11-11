from rest_framework import serializers

from webapp.models.parent import ParentModel


class ParentModelSerialize(serializers.ModelSerializer):
    class Meta:
        model = ParentModel
        fields = '__all__'
