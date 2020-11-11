from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from webapp.models.staff import StaffModel
from webapp.serializers.staffSerializer import StaffModelSerialize


class StaffCreateView(APIView):

    ''""" this block returns all the records''"""

    def get(self, request):
        staff = StaffModel.objects.all()
        emp_serialize_obj = StaffModelSerialize(staff, many=True)
        return Response(emp_serialize_obj.data, status=status.HTTP_200_OK)

    ''""" this method creates the new object''"""

    def post(self, request):
        stf_serial = StaffModelSerialize(data=request.data)
        if stf_serial.is_valid():
            stf_serial.save()
            print(type(stf_serial.data))
            return JsonResponse(stf_serial.data, status=status.HTTP_200_OK)
        return JsonResponse(status=status.HTTP_400_BAD_REQUEST)


''"""below part is for upgrading purpose and to retrieve specific details

staff update delete operations """


class StaffUpdate(APIView):

    def get_object(self, pk):
        ''""" it block checks if that 'pk' does have any value that can be used further''"""
        try:
            return StaffModel.objects.get(pk=pk)
        except StaffModel.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        ''"""this function gets a detail of a single object''"""
        staff = self.get_object(pk)
        serialize_obj = StaffModelSerialize(staff)
        return Response(serialize_obj.data)

    def put(self, request, pk):
        ''"""This function updates a particular object details''"""
        staff = self.get_object(pk)
        staff_serialize = StaffModelSerialize(staff, default=request.data)
        if staff_serialize.is_valid():
            staff_serialize.save()
            return Response(staff_serialize.data, status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        ''"""This function shits a particular object''"""
        emp_obj = self.get_object(pk)
        emp_obj.delete()
        return Response(status=status.HTTP_200_OK)
