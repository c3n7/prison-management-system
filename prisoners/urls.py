from django.urls import path

from .views import (
    PrisonersListView,
    PrisonersCreateView,
    PrisonersDetailView,
    PrisonersUpdateView,
)

urlpatterns = [
    path('<int:pk>/edit/',
         PrisonersUpdateView.as_view(),
         name='prisoners_edit'),
    path('<int:pk>/',
         PrisonersDetailView.as_view(),
         name='prisoners_detail'),
    path('new/',
         PrisonersCreateView.as_view(),
         name='prisoners_new'),
    path('',
         PrisonersListView.as_view(),
         name='prisoners_list'),
]
