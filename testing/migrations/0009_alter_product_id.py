# Generated by Django 5.0.1 on 2024-03-24 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0008_alter_product_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]