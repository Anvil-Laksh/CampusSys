# Generated by Django 3.1.3 on 2020-11-08 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoursesModel',
            fields=[
                ('course_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=20)),
                ('course_details', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='FacultyModel',
            fields=[
                ('faculty_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ParentModel',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='StaffModel',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('dob', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='StudentParentRelation',
            fields=[
                ('reg_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('Relation', models.CharField(max_length=20)),
                ('parent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.parentmodel')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.studentmodel')),
            ],
        ),
        migrations.CreateModel(
            name='StudentFacultyCourses',
            fields=[
                ('reg_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('course_details', models.CharField(max_length=20)),
                ('faculty_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.facultymodel')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.studentmodel')),
            ],
        ),
    ]
