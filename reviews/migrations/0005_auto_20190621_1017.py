# Generated by Django 2.2.1 on 2019-06-21 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_auto_20190621_0815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manga',
            name='cover',
            field=models.ImageField(default='covers/default.jpg', upload_to='covers/'),
        ),
    ]