# Generated by Django 2.0.5 on 2018-07-08 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sample_radius', '0003_auto_20180705_1827'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RadiusGroup',
        ),
        migrations.RemoveField(
            model_name='radiusgroupusers',
            name='radius_check',
        ),
        migrations.RemoveField(
            model_name='radiusgroupusers',
            name='radius_reply',
        ),
        migrations.DeleteModel(
            name='RadiusGroupUsers',
        ),
    ]
