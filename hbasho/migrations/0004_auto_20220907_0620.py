# Generated by Django 3.2.15 on 2022-09-07 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hbasho', '0003_auto_20220816_0403'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_by', models.IntegerField()),
                ('title', models.CharField(max_length=128)),
                ('division', models.CharField(choices=[('HBASHO_MAKUUCHI', 'Makuuchi'), ('HBASHO_JURYO', 'Juryo')], max_length=128)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(choices=[('HBASHO_TOKYO', 'Tokyo'), ('HBASHO_OSAKA', 'Osaka'), ('HBASHO_NAGOYA', 'Nagoya'), ('HBASHO_FUKUOKA', 'Fukuoka')], default='HBASHO_TOKYO', max_length=128)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TournamentWrestler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('withdrew', models.BooleanField(default=False)),
                ('shukun_prize', models.BooleanField(default=False)),
                ('kanto_prize', models.BooleanField(default=False)),
                ('gino_prize', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddConstraint(
            model_name='wrestlerprofile',
            constraint=models.UniqueConstraint(fields=('wrestler',), name='unique_wrestler_profile'),
        ),
        migrations.AddField(
            model_name='tournamentwrestler',
            name='rank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='hbasho.rank'),
        ),
        migrations.AddField(
            model_name='tournamentwrestler',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hbasho.tournament'),
        ),
        migrations.AddField(
            model_name='tournamentwrestler',
            name='wrestler',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hbasho.wrestler'),
        ),
        migrations.AddField(
            model_name='tournament',
            name='champion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='hbasho.wrestler'),
        ),
        migrations.AddConstraint(
            model_name='rank',
            constraint=models.UniqueConstraint(fields=('title',), name='unique_rank_title'),
        ),
        migrations.AddConstraint(
            model_name='tournamentwrestler',
            constraint=models.UniqueConstraint(fields=('wrestler', 'tournament'), name='unique_tournament_wrestler'),
        ),
    ]
