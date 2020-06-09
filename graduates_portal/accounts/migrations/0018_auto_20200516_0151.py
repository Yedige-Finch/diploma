# Generated by Django 2.1.2 on 2020-05-15 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_employer_student_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='course',
            field=models.CharField(choices=[('3', '3'), ('1', '1'), ('4', '4'), ('2', '2')], max_length=1),
        ),
        migrations.AlterField(
            model_name='student',
            name='speciality',
            field=models.CharField(choices=[('RET', 'RET'), ('IS', 'IS'), ('CSSE', 'CSSE')], max_length=12),
        ),
    ]
