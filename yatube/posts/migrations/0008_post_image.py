# Generated by Django 2.2.6 on 2021-07-04 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_remove_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='posts/'),
        ),
    ]
