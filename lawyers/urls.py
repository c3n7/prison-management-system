from django.urls import path

from .views import (
    LawyersCreateView,
    LawyersDetailView,
)

urlpatterns = [
    path('<int:pk>/',
         LawyersDetailView.as_view(),
         name='lawyers_detail'),
    path('new/',
         LawyersCreateView.as_view(),
         name='lawyers_new'),
]
