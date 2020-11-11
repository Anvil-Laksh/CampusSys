from django.db import models


class CoursesModel(models.Model):
    course_id = models.CharField(max_length=20, primary_key=True)
    course_name = models.CharField(max_length=20)
    course_details = models.CharField(max_length=20)

    def __str__(self):
        return self.course_id
