from webapp import models
from django.db import models


class StudentParentRelation(models.Model):
    reg_id = models.CharField(max_length=10, primary_key=True)
    student_id = models.ForeignKey('StudentModel', on_delete=models.CASCADE)
    parent_id = models.ForeignKey('ParentModel', on_delete=models.CASCADE)
    Relation = models.CharField(max_length=20)

    def __str__(self):
        return self.reg_id,


class StudentFacultyCourses(models.Model):
    reg_id = models.CharField(max_length=20, primary_key=True)
    student_id = models.ForeignKey('StudentModel', on_delete=models.CASCADE)
    faculty_id = models.ForeignKey('FacultyModel', on_delete=models.CASCADE)
    course_details = models.CharField(max_length=20)

    def __str__(self):
        return self.reg_id,
