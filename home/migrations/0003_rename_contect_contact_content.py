# Generated by Django 5.1.1 on 2024-10-14 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_contact_timestemp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='contect',
            new_name='content',
        ),
    ]
