# Generated by Django 4.2.5 on 2023-10-05 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_categoryitem_image_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoryitem',
            name='images',
            field=models.ImageField(default='', upload_to='media/image'),
        ),
    ]