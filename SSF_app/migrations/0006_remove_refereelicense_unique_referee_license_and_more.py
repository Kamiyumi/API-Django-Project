# Generated by Django 5.0.6 on 2024-06-21 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SSF_app', '0005_remove_lifterlicense_unique_license_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='refereelicense',
            name='unique_referee_license',
        ),
        migrations.AddField(
            model_name='refereelicense',
            name='requested_year',
            field=models.IntegerField(default=2024, editable=False),
            preserve_default=False,
        ),
        migrations.AddConstraint(
            model_name='refereelicense',
            constraint=models.UniqueConstraint(fields=('person', 'referee_license_nr', 'requested_year'), name='unique_referee_license'),
        ),
    ]
