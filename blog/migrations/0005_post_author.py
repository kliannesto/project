# Generated by Django 2.1.1 on 2019-11-14 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20191106_1110'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
