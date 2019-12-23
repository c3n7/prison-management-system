from django.urls import path

from .views import (
    NextOfKinCreateView,
    NextOfKinDetailView,
)

urlpatterns = [
    path('<int:pk>/',
         NextOfKinDetailView.as_view(),
         name='nextofkin_detail'),
    path('new/',
         NextOfKinCreateView.as_view(),
         name='nextofkin_new'),
]
