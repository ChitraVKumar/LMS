# Generated by Django 4.2.2 on 2023-06-24 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instructor_name', models.CharField(max_length=50)),
                ('instructor_mailid', models.CharField(max_length=50)),
                ('instructor_password', models.CharField(max_length=50)),
                ('instructor_bio', models.TextField()),
                ('instructor_specialization', models.CharField(max_length=150)),
                ('instructor_experience', models.IntegerField()),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='instructor_profiles/')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_username', models.CharField(max_length=50)),
                ('student_mailid', models.CharField(max_length=50)),
                ('student_password', models.CharField(max_length=50)),
                ('courses', models.TextField()),
                ('student_qualification', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='CourseCatalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
                ('course_description', models.TextField()),
                ('duration', models.IntegerField()),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.instructor')),
            ],
        ),
    ]
