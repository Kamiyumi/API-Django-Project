# Generated by Django 5.0.6 on 2024-06-23 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SSF_app', '0007_merge_20240623_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weightclass',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=255),
        ),
    ]
