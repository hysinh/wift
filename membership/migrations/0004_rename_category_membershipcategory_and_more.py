# Generated by Django 5.1.5 on 2025-01-30 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_rename_membership_purchase_membershippurchase'),
        ('membership', '0003_alter_category_options'),
        ('profiles', '0003_alter_member_data_private_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='MembershipCategory',
        ),
        migrations.AlterModelOptions(
            name='membershipcategory',
            options={'ordering': ['new_member_price', 'name'], 'verbose_name_plural': 'Membership Categories'},
        ),
    ]
