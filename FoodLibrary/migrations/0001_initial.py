# Generated by Django 3.2 on 2021-04-10 13:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('product_type', models.TextField()),
                ('ingredients', models.TextField()),
                ('produced_by', models.TextField()),
                ('weight', models.CharField(max_length=5)),
                ('standard_weight', models.CharField(max_length=5)),
                ('calories', models.CharField(max_length=5)),
                ('proteins', models.CharField(max_length=5)),
                ('carbohydrates', models.CharField(max_length=5)),
                ('fat', models.CharField(max_length=5)),
                ('fibre', models.CharField(max_length=5)),
                ('salt', models.CharField(max_length=5)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('product_image', models.ImageField(default='/static/img/default.png', upload_to='E:\\Zajęcia\\djangoProject1\\FoodCalories\\media')),
                ('additional_image', models.ImageField(blank=True, upload_to='additional')),
                ('miniature_image', models.ImageField(blank=True, upload_to='minis')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('approved_comment', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='FoodLibrary.product')),
            ],
        ),
    ]
