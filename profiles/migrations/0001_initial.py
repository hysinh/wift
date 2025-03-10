# Generated by Django 5.1.5 on 2025-01-28 13:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('membership', '0003_alter_category_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberProfile_Private',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default_firstname', models.CharField(max_length=80)),
                ('default_lastname', models.CharField(max_length=80)),
                ('default_street_address1', models.CharField(max_length=80)),
                ('default_street_address2', models.CharField(max_length=80)),
                ('default_town_or_city', models.CharField(max_length=40)),
                ('default_county', models.CharField(max_length=80)),
                ('default_postcode', models.CharField(max_length=20)),
                ('default_country', models.CharField(blank=True, max_length=20, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=0)),
                ('member', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('membership_level', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='membership.category')),
            ],
            options={
                'ordering': ['default_lastname', 'default_firstname'],
            },
        ),
    ]
