from django.db import models
from pytz import timezone

class Forecast(models.Model):
    creation_time = models.DateTimeField('Forecast Creation Time')
    prediction_time = models.DateTimeField('Forecast Datetime', primary_key=True)
    mean_air_temp = models.FloatField('Mean Air Temperature')
    max_air_temp = models.FloatField('Max Air Temperature')
    min_air_temp = models.FloatField('Min Air Temperature')
    mean_l_precip_rate = models.FloatField('Mean Liquid Precipitation Rate')
    max_l_precip_rate = models.FloatField('Max Liquid Precipitation Rate')
    min_l_precip_rate = models.FloatField('Min Liquid Precipitation Rate')
    mean_s_precip_rate = models.FloatField('Mean Solid Precipitation Rate')
    max_s_precip_rate = models.FloatField('Max Solid Precipitation Rate')
    min_s_precip_rate = models.FloatField('Min Solid Precipitation Rate')
    mean_wind_speed = models.FloatField('Mean Wind Speed')
    max_wind_speed = models.FloatField('Max Wind Speed')
    min_wind_speed = models.FloatField('Min Wind Speed')
    mean_wind_dir = models.FloatField('Mean Wind Direction')
    max_wind_dir = models.FloatField('Max Wind Direction')
    min_wind_dir = models.FloatField('Min Wind Direction')
    mean_pressure = models.FloatField('Mean Pressure')
    max_pressure = models.FloatField('Max Pressure')
    min_pressure = models.FloatField('Min Pressure')
    mean_humidity = models.FloatField('Mean Humidity')
    max_humidity = models.FloatField('Max Humidity')
    min_humidity = models.FloatField('Min Humidity')

    def __str__(self):
        tz = timezone("America/Vancouver")
        return self.creation_time.astimezone(tz).strftime('%Y-%m-%d %H:%M') + " | " + self.prediction_time.astimezone(tz).strftime('%Y-%m-%d %H:%M')

class Condition(models.Model):
    time = models.DateTimeField('Datetime', primary_key=True)
    air_temp = models.FloatField("Air Temperature")
    l_precip_rate = models.FloatField("Liquid Precipitation Rate")
    wind_speed = models.FloatField("Wind Speed")
    wind_dir = models.FloatField("Wind Direction")
    pressure = models.FloatField("Pressure")
    brightness = models.FloatField("Solar Radiation")
    humidity = models.FloatField("Humidity")

    def __str__(self):
        tz = timezone("America/Vancouver")
        return self.time.astimezone(tz).strftime('%Y-%m-%d %H:%M')
