# Generated by Django 2.1.1 on 2018-09-05 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppingitem',
            name='quantity',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]