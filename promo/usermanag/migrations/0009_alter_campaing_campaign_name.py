# Generated by Django 4.0.3 on 2022-05-07 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanag', '0008_alter_campaigndata_camp_num_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaing',
            name='campaign_name',
            field=models.CharField(max_length=200, unique=True, verbose_name='Название кампании'),
        ),
    ]