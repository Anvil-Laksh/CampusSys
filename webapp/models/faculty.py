from django.db import models


class FacultyModel(models.Model):
    faculty_id = models.CharField(max_length=20, primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)

    def __str__(self):
        return self.email,
