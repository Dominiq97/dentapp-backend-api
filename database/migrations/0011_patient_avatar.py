# Generated by Django 3.0.8 on 2021-06-20 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0010_auto_20210620_2132'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='avatar',
            field=models.ImageField(default='eee', upload_to='media/patients/avatars/'),
            preserve_default=False,
        ),
    ]
