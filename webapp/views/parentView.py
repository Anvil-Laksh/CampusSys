from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from webapp.models.parent import ParentModel
from webapp.serializers.parentSerializer import ParentModelSerialize


class ParentDetailView(APIView):

    def check_object(self, pk):
        ''""" it block checks if that 'pk' does have any value that can be used further''"""
        try:
            return ParentModel.objects.get(pk=pk)
        except ParentModel.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        ''"""this function gets a detail of a single object''"""
        parent_obj = self.check_object(pk)
        parent_serialize = ParentModelSerialize(parent_obj)
        return Response(parent_serialize.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        ''"""This function updates a particular object details''"""
        parent_obj = self.check_object(pk)
        parent_serialize = ParentModelSerialize(parent_obj, default=request.data)
        if parent_serialize.is_valid():
            parent_serialize.save()
            return Response(parent_serialize.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
