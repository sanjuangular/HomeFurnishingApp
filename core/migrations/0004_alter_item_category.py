# Generated by Django 4.2.4 on 2023-08-28 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_item_category_alter_item_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='core.category'),
        ),
    ]
