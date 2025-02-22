# Generated by Django 5.0.2 on 2025-02-21 16:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_category_products_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255, verbose_name='Category1')),
                ('slug', models.SlugField(unique=True, verbose_name='Manzil')),
            ],
            options={
                'verbose_name': 'Category1',
                'verbose_name_plural': 'categor',
            },
        ),
        migrations.RemoveField(
            model_name='products',
            name='category',
        ),
        migrations.AddField(
            model_name='products',
            name='category1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categor', to='store.category1'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
