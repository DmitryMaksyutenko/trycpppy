# Generated by Django 3.1.3 on 2021-03-07 12:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20210306_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='image',
            field=models.FileField(blank=True, max_length=132, null=True, upload_to='', validators=[django.core.validators.FileExtensionValidator(['svg'])]),
        ),
    ]
