# Generated by Django 4.1.6 on 2023-04-30 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_alter_figure_figure_set'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='figure_set',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='game.figureset'),
        ),
        migrations.AlterField(
            model_name='player',
            name='health',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='player',
            name='name',
            field=models.CharField(help_text='Vad vill du kalla dig i detta spelet?', max_length=50),
        ),
        migrations.AlterField(
            model_name='player',
            name='profile',
            field=models.ImageField(help_text='Vilken profilbild vill du ha i spelet?', upload_to='profiles/% Y/% m/% d/'),
        ),
    ]