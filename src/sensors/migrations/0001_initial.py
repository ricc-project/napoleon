# Generated by Django 2.2.1 on 2019-05-10 21:08

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
            name='DataCluster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collected_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WindData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speed', models.FloatField()),
                ('direction', models.PositiveIntegerField()),
                ('data_cluster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sensors.DataCluster')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SolarData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('radiation', models.PositiveIntegerField()),
                ('data_cluster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sensors.DataCluster')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SoilData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moisture', models.FloatField()),
                ('temperature', models.FloatField()),
                ('data_cluster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sensors.DataCluster')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RainData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rainfall', models.PositiveIntegerField()),
                ('data_cluster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sensors.DataCluster')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AirData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('humidity', models.FloatField()),
                ('temperature', models.FloatField()),
                ('pressure', models.FloatField()),
                ('data_cluster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sensors.DataCluster')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ActuatorData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('data_cluster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sensors.DataCluster')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]