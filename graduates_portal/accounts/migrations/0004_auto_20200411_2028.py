# Generated by Django 2.1.2 on 2020-04-11 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200411_2006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employer',
            name='сс_approve',
        ),
        migrations.AddField(
            model_name='employer',
            name='login',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AddField(
            model_name='student',
            name='birth',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='employer',
            name='face',
            field=models.CharField(choices=[('S', 'Student'), ('E', 'Employer'), ('A', 'Admin')], default='A', max_length=3),
        ),
        migrations.AlterField(
            model_name='student',
            name='course',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='face',
            field=models.CharField(choices=[('S', 'Student'), ('E', 'Employer'), ('A', 'Admin')], default='S', max_length=3),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='speciality',
            field=models.CharField(max_length=12),
        ),
    ]
