# Generated by Django 5.1.2 on 2024-10-22 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0006_skill_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='skillcategory',
            name='description',
            field=models.TextField(default='default'),
            preserve_default=False,
        ),
    ]