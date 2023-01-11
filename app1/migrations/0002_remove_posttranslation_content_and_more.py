# Generated by Django 4.1.5 on 2023-01-11 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posttranslation',
            name='content',
        ),
        migrations.AddField(
            model_name='posttranslation',
            name='description',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='posttranslation',
            name='short_description',
            field=models.CharField(blank=True, max_length=200, verbose_name='Short Description'),
        ),
    ]