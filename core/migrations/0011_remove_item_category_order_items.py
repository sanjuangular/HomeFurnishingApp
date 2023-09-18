# Generated by Django 4.2.4 on 2023-08-29 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_item_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='category',
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(through='core.CartItem', to='core.item'),
        ),
    ]
