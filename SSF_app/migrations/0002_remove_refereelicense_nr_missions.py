# Generated by Django 5.0.6 on 2024-06-10 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SSF_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='refereelicense',
            name='nr_missions',
        ),
    ]
