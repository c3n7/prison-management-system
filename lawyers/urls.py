from django.urls import path

from .views import (
    LawyersCreateView,
    LawyersDetailView,
)

urlpatterns = [
    path('<int:pk>/',
         LawyersDetailView.as_view(),
         name='prisoners_detail'),
    path('new/',
         LawyersCreateView.as_view(),
         name='prisoners_new'),
]
