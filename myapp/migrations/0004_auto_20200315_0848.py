# Generated by Django 2.2.9 on 2020-03-15 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20200315_0845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='cast',
            field=models.CharField(default='', max_length=5500),
        ),
    ]