# Generated by Django 5.1.3 on 2024-11-09 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookHub', '0003_alter_book_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='page',
            field=models.IntegerField(default=0),
        ),
    ]