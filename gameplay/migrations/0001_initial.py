# Generated by Django 2.0.3 on 2018-03-29 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('last_play', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Move',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
                ('comment', models.CharField(blank=True, max_length=100)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='moves', to='gameplay.Game')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('score', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='move',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='moves', to='gameplay.User'),
        ),
        migrations.AddField(
            model_name='game',
            name='current_player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pending_turns', to='gameplay.User'),
        ),
    ]
