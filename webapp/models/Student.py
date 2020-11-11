from django.db import models


class StudentModel(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    dob = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)

    def __str__(self):
        return self.email
