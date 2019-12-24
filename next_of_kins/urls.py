from django.urls import path

from .views import (
    NextOfKinCreateView,
    NextOfKinDetailView,
    KinPrisonerCreateView,
    KinPrisonerListView,
    KinPrisonerDeleteView
)

urlpatterns = [
    path('<int:pk>/',
         NextOfKinDetailView.as_view(),
         name='nextofkin_detail'),
    path('new/',
         NextOfKinCreateView.as_view(),
         name='nextofkin_new'),
    path('kinprisoners/new/',
         KinPrisonerCreateView.as_view(),
         name='kinprisoners_new'),
    path('kinprisoners/<int:pk>/delete/',
         KinPrisonerDeleteView.as_view(),
         name='kinprisoners_delete'),
    path('kinprisoners/',
         KinPrisonerListView.as_view(),
         name='kinprisoners_list'),
]
