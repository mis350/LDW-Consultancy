# Generated by Django 3.2.4 on 2021-06-29 23:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20210628_2110'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookstatus',
            options={'ordering': ['due_back'], 'permissions': (('can_mark_returned', 'Set book as returned'),), 'verbose_name_plural': 'Book Statuses'},
        ),
    ]