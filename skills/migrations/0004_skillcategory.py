# Generated by Django 5.1.2 on 2024-10-22 05:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkillCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
                ('belongCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skills.skill')),
            ],
        ),
    ]
