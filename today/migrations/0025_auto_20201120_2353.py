# Generated by Django 3.1.2 on 2020-11-20 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('today', '0024_auto_20201120_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='studio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='studio_review', to='today.product'),
        ),
    ]