# Generated by Django 3.1.2 on 2020-11-19 04:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('today', '0014_remove_review_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Review',
        ),
    ]
