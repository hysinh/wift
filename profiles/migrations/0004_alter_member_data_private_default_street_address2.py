# Generated by Django 5.1.5 on 2025-02-10 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_alter_member_data_private_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member_data_private',
            name='default_street_address2',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
