# Generated by Django 4.0.3 on 2022-04-24 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanag', '0003_alter_campaing_id_campaign_alter_poll_id_poll_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='id_house',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]