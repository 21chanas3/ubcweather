from django.urls import path

from . import views

urlpatterns = [
    path('current/', views.CurrentConditionView.as_view(), name='current-conditions'),
    path('past/', views.PastWeekConditionsView.as_view(), name='past-conditions')
]