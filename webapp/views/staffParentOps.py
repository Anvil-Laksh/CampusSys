from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from webapp.models.parent import ParentModel
from webapp.serializers.parentSerializer import ParentModelSerialize


class CreateViewParent(APIView):
    def get(self, request):
        parent_obj = ParentModel.objects.all()
        parent_serialize_obj = ParentModelSerialize(parent_obj, many=True)
        return Response(parent_serialize_obj.data, status=status.HTTP_200_OK)

    def post(self, request):
        serialize_obj = ParentModelSerialize(data=request.data)
        if serialize_obj.is_valid():
            serialize_obj.save()
            return Response(serialize_obj.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class AlterDelParent(APIView):

    def get_object(self, pk):
        ''""" it block checks if that 'pk' does have any value that can be used further''"""
        try:
            return ParentModel.objects.get(pk=pk)
        except ParentModel.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        ''"""this function gets a detail of a single object''"""
        parent_obj = self.get_object(pk)
        parent_serialize = ParentModelSerialize(parent_obj)
        return Response(parent_serialize.data)

    def put(self, request, pk):
        ''"""This function updates a particular object details''"""
        parent_obj = self.get_object(pk)
        parent_serialize = ParentModelSerialize(parent_obj, default=request.data)
        if parent_serialize.is_valid():
            parent_serialize.save()
            return Response(parent_serialize.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        parent_obj = self.get_object(pk)
        parent_obj.delete()
        return Response(status=status.HTTP_200_OK)
