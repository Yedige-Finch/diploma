# Generated by Django 2.1.2 on 2020-05-15 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_employer_student_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='course',
            field=models.CharField(choices=[('4', '4'), ('3', '3'), ('1', '1'), ('2', '2')], max_length=1),
        ),
        migrations.AlterField(
            model_name='student',
            name='speciality',
            field=models.CharField(choices=[('RET', 'RET'), ('CSSE', 'CSSE'), ('IS', 'IS')], max_length=12),
        ),
    ]
