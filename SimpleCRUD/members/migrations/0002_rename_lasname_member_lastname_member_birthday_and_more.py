# Generated by Django 4.1.6 on 2023-02-07 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='birthday',
            field=models.DateField(default='1000-01-01'),
        ),
        migrations.AddField(
            model_name='member',
            name='email',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='joineddate',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='password',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='userid',
            field=models.CharField(default='xxxxx', max_length=10),
        ),
    ]
