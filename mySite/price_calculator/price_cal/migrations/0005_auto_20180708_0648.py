# Generated by Django 2.0.6 on 2018-07-08 06:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price_cal', '0004_auto_20180708_0644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cal',
            name='compare_date',
            field=models.DateField(default=datetime.date(2018, 7, 8)),
        ),
    ]
