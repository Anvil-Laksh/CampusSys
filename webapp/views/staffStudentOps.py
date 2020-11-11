import rest_framework
from rest_framework.response import Response
from rest_framework.views import APIView
from webapp.models.Student import StudentModel
from webapp.serializers.studentSerializer import StudentModelSerialize
from rest_framework import status


class CreateStudent(APIView):
    def post(self, request):
        serialize_obj: StudentModelSerialize = StudentModelSerialize(data=request.data)
        if serialize_obj.is_valid():
            serialize_obj.save()
            return Response(serialize_obj.data, status=rest_framework.status.HTTP_201_CREATED)
        return Response(status=rest_framework.status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        student_obj = StudentModel.objects.all()
        student_serialize_obj = StudentModelSerialize(student_obj, many=True)
        return Response(student_serialize_obj.data, status=rest_framework.status.HTTP_200_OK)


class AlterDelStudent(APIView):

    def get_object(self, pk):
        ''""" it block checks if that 'pk' does have any value that can be used further''"""
        try:
            return StudentModel.objects.get(pk=pk)
        except StudentModel.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        ''"""this function gets a detail of a single object''"""
        student_obj = self.get_object(pk)
        student_serialize = StudentModelSerialize(student_obj,status=status.HTTP_200_OK)
        return Response(student_serialize.data,status=status.HTTP_200_OK)

    def put(self, request, pk):
        ''"""This function updates a particular object details''"""
        student_obj = self.get_object(pk)
        student_serialize = StudentModelSerialize(student_obj, default=request.data)
        if student_serialize.is_valid():
            student_serialize.save()
            return Response(student_serialize.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        ''"""This function shits a particular object''"""
        student_obj = self.get_object(pk)
        student_obj.delete()
        return Response(status=status.HTTP_200_OK)
