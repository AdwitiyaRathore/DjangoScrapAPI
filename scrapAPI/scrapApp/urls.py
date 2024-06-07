from django.urls import path

from .views import *

urlpatterns = [
    path('postScrap/', StartScrapingView.as_view()),
    path('getScrap/<int:job_id>', ScrapingStatusView.as_view()),
]