# Generated by Django 4.0.3 on 2022-04-24 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usermanag', '0004_alter_house_id_house'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaigndata',
            name='poll_camp',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usermanag.poll'),
        ),
        migrations.AlterField(
            model_name='campaigndata',
            name='poll_form_camp',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usermanag.poolform'),
        ),
    ]
