# Generated by Django 4.1.5 on 2023-01-13 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('time', models.DateTimeField(primary_key=True, serialize=False, verbose_name='Datetime')),
                ('air_temp', models.FloatField(verbose_name='Air Temperature')),
                ('l_precip_rate', models.FloatField(verbose_name='Liquid Precipitation Rate')),
                ('wind_speed', models.FloatField(verbose_name='Wind Speed')),
                ('wind_dir', models.FloatField(verbose_name='Wind Direction')),
                ('pressure', models.FloatField(verbose_name='Pressure')),
                ('brightness', models.FloatField(verbose_name='Solar Radiation')),
                ('humidity', models.FloatField(verbose_name='Humidity')),
            ],
        ),
        migrations.CreateModel(
            name='Forecast',
            fields=[
                ('creation_time', models.DateTimeField(verbose_name='Forecast Creation Time')),
                ('prediction_time', models.DateTimeField(primary_key=True, serialize=False, verbose_name='Forecast Datetime')),
                ('mean_air_temp', models.FloatField(verbose_name='Mean Air Temperature')),
                ('max_air_temp', models.FloatField(verbose_name='Max Air Temperature')),
                ('min_air_temp', models.FloatField(verbose_name='Min Air Temperature')),
                ('mean_l_precip_rate', models.FloatField(verbose_name='Mean Liquid Precipitation Rate')),
                ('max_l_precip_rate', models.FloatField(verbose_name='Max Liquid Precipitation Rate')),
                ('min_l_precip_rate', models.FloatField(verbose_name='Min Liquid Precipitation Rate')),
                ('mean_s_precip_rate', models.FloatField(verbose_name='Mean Solid Precipitation Rate')),
                ('max_s_precip_rate', models.FloatField(verbose_name='Max Solid Precipitation Rate')),
                ('min_s_precip_rate', models.FloatField(verbose_name='Min Solid Precipitation Rate')),
                ('mean_wind_speed', models.FloatField(verbose_name='Mean Wind Speed')),
                ('max_wind_speed', models.FloatField(verbose_name='Max Wind Speed')),
                ('min_wind_speed', models.FloatField(verbose_name='Min Wind Speed')),
                ('mean_wind_dir', models.FloatField(verbose_name='Mean Wind Direction')),
                ('max_wind_dir', models.FloatField(verbose_name='Max Wind Direction')),
                ('min_wind_dir', models.FloatField(verbose_name='Min Wind Direction')),
                ('mean_pressure', models.FloatField(verbose_name='Mean Pressure')),
                ('max_pressure', models.FloatField(verbose_name='Max Pressure')),
                ('min_pressure', models.FloatField(verbose_name='Min Pressure')),
                ('mean_humidity', models.FloatField(verbose_name='Mean Humidity')),
                ('max_humidity', models.FloatField(verbose_name='Max Humidity')),
                ('min_humidity', models.FloatField(verbose_name='Min Humidity')),
            ],
        ),
    ]
