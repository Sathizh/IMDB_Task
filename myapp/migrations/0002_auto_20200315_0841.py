# Generated by Django 2.2.9 on 2020-03-15 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movies',
            name='writter',
        ),
        migrations.AddField(
            model_name='movies',
            name='writer',
            field=models.CharField(default='', max_length=500),
        ),
    ]