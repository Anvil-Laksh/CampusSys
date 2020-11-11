from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from webapp.models.Student import StudentModel
from webapp.serializers.studentSerializer import StudentModelSerialize


class StudentDetailView(APIView):

    def check_object(self, pk):
        ''""" it block checks if that 'pk' does have any value that can be used further''"""
        try:
            return StudentModel.objects.get(pk=pk)
        except StudentModel.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        ''"""this function gets a detail of a single object''"""
        student_obj = self.check_object(pk)
        student_serialize = StudentModelSerialize(student_obj)
        return Response(student_serialize.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        ''"""This function updates a particular object details''"""
        student_obj = self.check_object(pk)
        student_serialize = StudentModelSerialize(student_obj, default=request.data)
        if student_serialize.is_valid():
            student_serialize.save()
            return Response(student_serialize.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
