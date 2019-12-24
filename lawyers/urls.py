from django.urls import path

from .views import (
    LawyersCreateView,
    LawyersDetailView,
    LawyerClientListView,
    LawyerClientCreateView,
    LawyerClientDeleteView,
)

urlpatterns = [
    path('<int:pk>/',
         LawyersDetailView.as_view(),
         name='lawyers_detail'),
    path('new/',
         LawyersCreateView.as_view(),
         name='lawyers_new'),
    path('clients/new/',
         LawyerClientCreateView.as_view(),
         name='lawyerclients_new'),
    path('clients/<int:pk>/delete/',
         LawyerClientDeleteView.as_view(),
         name='lawyerclients_delete'),
    path('clients/',
         LawyerClientListView.as_view(),
         name='lawyerclients_list'),
]
