# Generated by Django 4.2.4 on 2023-08-28 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_item_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='category',
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
