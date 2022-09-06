# Generated by Django 3.2.15 on 2022-09-06 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hbasho', '0004_tournament'),
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
        migrations.AlterField(
            model_name='tournament',
            name='location',
            field=models.CharField(choices=[('HBASHO_TOKYO', 'Tokyo'), ('HBASHO_OSAKA', 'Osaka'), ('HBASHO_NAGOYA', 'Nagoya'), ('HBASHO_FUKUOKA', 'Fukuoka')], default='HBASHO_TOKYO', max_length=128),
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
                ('rank', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='hbasho.rank')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hbasho.tournament')),
                ('wrestler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hbasho.wrestler')),
            ],
        ),
    ]