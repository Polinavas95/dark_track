from django.urls import path
from .import views

urlpatterns = [
    path('', views.TractorTrackView.as_view(), name='index'),
]
