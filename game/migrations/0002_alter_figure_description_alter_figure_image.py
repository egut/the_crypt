# Generated by Django 4.1.6 on 2023-04-22 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='figure',
            name='description',
            field=models.TextField(help_text='Description of the figure'),
        ),
        migrations.AlterField(
            model_name='figure',
            name='image',
            field=models.ImageField(blank=True, upload_to='figures'),
        ),
    ]
