# Generated by Django 2.2.7 on 2019-11-27 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blockoo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='boardmodel',
            name='currentPlayer',
            field=models.CharField(default='red', max_length=6),
            preserve_default=False,
        ),
    ]
