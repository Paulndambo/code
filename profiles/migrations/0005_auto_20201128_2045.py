# Generated by Django 3.1.2 on 2020-11-28 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_profile_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, default='Nairobi', max_length=200, null=True),
        ),
    ]
