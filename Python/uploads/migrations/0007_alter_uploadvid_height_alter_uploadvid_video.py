# Generated by Django 5.0.4 on 2024-05-05 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0006_uploadvid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadvid',
            name='height',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='uploadvid',
            name='video',
            field=models.FileField(upload_to='video/'),
        ),
    ]