# Generated by Django 4.0.3 on 2022-06-20 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanag', '0009_alter_campaing_campaign_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house',
            name='city',
        ),
        migrations.RemoveField(
            model_name='house',
            name='house_number',
        ),
        migrations.RemoveField(
            model_name='house',
            name='street',
        ),
        migrations.AddField(
            model_name='house',
            name='address',
            field=models.CharField(default='default title', max_length=400, verbose_name='Адрес'),
        ),
    ]
