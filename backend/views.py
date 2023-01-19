from rest_framework import generics, views, response
from .serializers import ConditionSerializer, ForecastSerializer
from .models import Condition, Forecast
from datetime import datetime, timedelta
import pytz

# Create your views here.
class CurrentConditionView(views.APIView):
    def get(self, request):
        latest_instance = Condition.objects.latest('time')
        serializer = ConditionSerializer(latest_instance)
        return response.Response(serializer.data)

class PastWeekConditionsView(generics.ListAPIView):
    tz = pytz.timezone("America/Vancouver")
    from_date = datetime.now(tz) - timedelta(days=7)
    queryset= Condition.objects.filter(time__gte = from_date)
    serializer_class = ConditionSerializer