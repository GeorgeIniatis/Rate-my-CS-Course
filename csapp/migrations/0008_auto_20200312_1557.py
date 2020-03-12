# Generated by Django 2.2.3 on 2020-03-12 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('csapp', '0007_courserating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='year_in_uni',
            new_name='year_in_university',
        ),
        migrations.DeleteModel(
            name='CourseRating',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
