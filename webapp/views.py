# from django.shortcuts import render
# from rest_framework import viewsets
# # Create your views here.
# from webapp.models import StudentModel, StaffModel, StudentFacultyCourses, StudentParentRelation, ParentModel, \
#     FacultyModel, CoursesModel
# from webapp.serializer import StudentModelSerialize, StaffModelSerialize, ParentModelSerialize, \
#     StudentFacultyCoursesSerialize, StudentParentRelationSerialize, FacultyModelSerialize, CoursesModelSerialize
#
#
#
#
#
#
#
#
# class ParentCrud(viewsets.ModelViewSet):
#     queryset = ParentModel.objects.all()
#     serializer_class = ParentModelSerialize
#
#
# class StudentParentCrud(viewsets.ModelViewSet):
#     queryset = StudentParentRelation.objects.all()
#     serializer_class = StudentParentRelationSerialize
#
#
# class FacultyCrud(viewsets.ModelViewSet):
#     queryset = FacultyModel.objects.all()
#     serializer_class = FacultyModelSerialize
#
#
# class StudentFacultyCrud(viewsets.ModelViewSet):
#     queryset = StudentFacultyCourses.objects.all()
#     serializer_class = StudentFacultyCoursesSerialize
#
#
# class CoursesCrud(viewsets.ModelViewSet):
#     queryset = CoursesModel.objects.all()
#     serializer_class = CoursesModelSerialize
#
#
#
