# Generated by Django 4.1.6 on 2023-04-09 14:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FigureSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of the game', max_length=100, unique=True)),
                ('start_time', models.DateTimeField(help_text='When the game will start')),
            ],
        ),
        migrations.CreateModel(
            name='GameConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of the game configuration', max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Phalanx',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of the phalanx', max_length=50)),
                ('description', models.TextField(blank=True)),
                ('game_config', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='game.gameconfig')),
                ('parent_phalanx', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='game.phalanx')),
            ],
        ),
        migrations.CreateModel(
            name='Victory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('win_condition', models.CharField(choices=[('ALL_OTHER', 'All Other'), ('PHALANX', 'Phalanx')], help_text='What kind of win condition?', max_length=20)),
                ('phalanx', models.ForeignKey(help_text='To what phalanx is this win condition for', on_delete=django.db.models.deletion.CASCADE, to='game.phalanx')),
                ('win_condition_argument', models.OneToOneField(help_text='How do it relate to, if any?', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='game.phalanx')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('profile', models.ImageField(upload_to='profiles')),
                ('health', models.IntegerField()),
                ('figure_set', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='game.figureset')),
                ('game', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='game.game')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='game_config',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.gameconfig'),
        ),
        migrations.CreateModel(
            name='Figure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='The name of the figure', max_length=50)),
                ('description', models.TextField(help_text='DEscription of the figure')),
                ('image', models.ImageField(upload_to='figures')),
                ('type', models.CharField(choices=[('PROFESSION', 'Profession'), ('PERSONAGE', 'Personage'), ('ALONE', 'Alone')], help_text='What kind of figure is this?', max_length=20)),
                ('figure_set', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='game.figureset')),
                ('phalanx', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.phalanx')),
            ],
        ),
        migrations.CreateModel(
            name='Effect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('number_of_usage', models.IntegerField()),
                ('type', models.CharField(choices=[('ATTACK', 'Attack'), ('DEFENSE', 'Defense'), ('LOOKUP', 'Lookup')], help_text='What kind of action?', max_length=20)),
                ('value', models.IntegerField()),
                ('figure', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='game.figure')),
            ],
        ),
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('number_of_usage', models.IntegerField()),
                ('type', models.CharField(choices=[('ATTACK', 'Attack'), ('DEFENSE', 'Defense'), ('LOOKUP', 'Lookup')], help_text='What kind of action?', max_length=20)),
                ('value', models.IntegerField()),
                ('phalanx', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.phalanx')),
            ],
        ),
    ]
