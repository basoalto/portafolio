# Generated by Django 4.0.5 on 2022-06-27 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='description',
            field=models.TextField(),
        ),
    ]