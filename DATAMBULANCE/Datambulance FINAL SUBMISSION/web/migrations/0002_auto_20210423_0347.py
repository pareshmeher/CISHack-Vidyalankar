# Generated by Django 3.2 on 2021-04-22 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AddField(
            model_name='prescription',
            name='desc',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='prescription',
            name='title',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
