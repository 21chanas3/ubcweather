from .models import Condition, Forecast
from rest_framework import serializers


class ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condition
        exclude = ['id']


class ForecastSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Forecast
        exclude = ['id']