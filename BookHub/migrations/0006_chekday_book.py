# Generated by Django 5.1.3 on 2024-11-18 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookHub', '0005_chekday'),
    ]

    operations = [
        migrations.AddField(
            model_name='chekday',
            name='book',
            field=models.ManyToManyField(to='BookHub.book'),
        ),
    ]