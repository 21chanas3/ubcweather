import pandas as pd
import numpy as np
import pytz
from datetime import datetime, timedelta
import urllib.request
import math
from backend.models import Condition, Forecast
import os

def get_data(date):
    dateString = date.strftime('%y%m%d')
    f = urllib.request.urlopen(os.environ['DATA_URL'] + dateString + "00").read().decode("utf-8")
    arr = f.split('\n\n\n')
    arr[0] = arr[0].split("\n",3)[3]
    arr[1] = arr[1].split("\n",1)[1]
    arr[2] = arr[2].split("\n",2)
    return arr      

def get_date():
    tz = pytz.timezone("America/Vancouver")
    ubcTime = datetime.now(tz)
    return ubcTime

def get_forecast_frame(arr):
    f = open("backend/management/commands/forecast_headers.txt", "r")
    headers = [f.read().split('\n')]
    data = np.zeros(shape=(84,28))
    counter = 0
    split = arr.split("\n")
    for line in split:
        newArr = np.fromstring(line, dtype=float, count=28, sep=" ")
        data[counter] = newArr
        counter += 1
    forecastFrame = pd.DataFrame(data, columns=headers)
    return forecastFrame
    
def get_previous_conditions(arr, date):
    f = open("headers/past_condition_headers.txt", "r")
    headers = f.read().split('\n')
    minRows = 347
    now = date
    elapsedTime = now - now.replace(hour=0, minute=0, second=0, microsecond=0)
    generatedRows = math.floor(elapsedTime.total_seconds() / 60 / 15)
    currRows = minRows + generatedRows
    data = np.zeros(shape=(currRows,10))
    counter = 0
    split = arr[1].split("\n")
    for line in split:
        newArr = np.fromstring(line, dtype=float, count=10, sep=" ")
        data[counter] = newArr
        counter += 1
    conditionsFrame = pd.DataFrame(data, columns=headers)
    conditionsFrame = conditionsFrame.set_index('Hour', drop=True)
    return conditionsFrame
    
def get_current(arr, arr2):
    condition = Condition()
    headers = ["Time", "AirTemp", "Dewpoint", "Humidity", "Pressure", "PressureTrend", "WindSpeed", "WindChill", "RainToday", "RainRate", "WindFrom"]
    timestamp = arr[1]
    data = arr[2]
    data2 = arr2.split("\n").pop().split(" ")
    condArr = data.split("\n")[:10]
    condArr.insert(0, int(timestamp))
    condDict = {headers[i]: condArr[i] for i in range(0, len(headers), 1)}
    condition.air_temp = condDict.get("AirTemp")
    condition.humidity = condDict.get("Humidity")
    condition.pressure = condDict.get("Pressure")
    condition.wind_speed = condDict.get("WindSpeed")
    condition.l_precip_rate = condDict.get("RainRate")
    condition.wind_dir = data2[5]
    condition.brightness = data2[8]
    tz = pytz.timezone("America/Vancouver")
    condition.time = tz.localize(datetime.strptime(timestamp, '%Y%m%d%H%M'))
    return condition
    
def get_current_conditions():
    date = get_date()
    date = date - timedelta(minutes=1)
    data = get_data(date)
    current = get_current(data[2], data[1])
    current.save()
    print("Obtained conditions for " + date.strftime('%Y/%m/%d %H:%M'))
    return

def get_forecast():
    date = get_date()
    date = date - timedelta(minutes=1)
    data = get_data(date)
    forecast_frame = get_forecast_frame(data[0])
    tz = pytz.timezone("America/Vancouver")
    basetime = tz.localize(date.replace(hour=0, minute=0, second=0, microsecond=0))
    for index, row in forecast_frame.iterrows():
        forecast = Forecast()
        if (row.name < 7):
            continue
        forecast.creation_time = basetime
        forecast.prediction_time = basetime + timedelta(hours=row.name - 7)
        forecast.mean_air_temp = row["MeanAirTemp"]
        forecast.min_air_temp = row["MinAirTemp"]
        forecast.max_air_temp = row["MaxAirTemp"]
        forecast.mean_l_precip_rate = row["LPrecipRateMean"]
        forecast.min_l_precip_rate = row["LPrecipRateMin"]
        forecast.max_l_precip_rate = row["LPrecipRateMax"]
        forecast.mean_s_precip_rate = row["SPrecipRateMean"]
        forecast.min_s_precip_rate = row["SPrecipRateMin"]
        forecast.max_s_precip_rate = row["SPrecipRateMax"]
        forecast.mean_wind_speed = row["WindSpeedMean"]
        forecast.max_wind_speed = row["WindSpeedMax"]
        forecast.min_wind_speed = row["WindSpeedMin"]
        forecast.mean_wind_dir = row["WindDirMean"]
        forecast.max_wind_dir = row["WindDirMax"]
        forecast.min_wind_dir = row["WindDirMin"]
        forecast.mean_pressure = row["PressureMean"]
        forecast.max_pressure = row["PressureMax"]
        forecast.min_pressure = row["PressureMin"]
        forecast.mean_humidity = row["HumidityMean"]
        forecast.max_humidity = row["HumidityMax"]
        forecast.min_humidity = row["HumidityMin"]
        forecast.save()
    print("Obtained forecast for " + basetime.strftime('%Y/%m/%d'))
    deleteSet = Forecast.objects.filter(prediction_time__lt=basetime)
    for model in deleteSet:
        model.delete()
