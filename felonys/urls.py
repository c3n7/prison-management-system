from django.urls import path

from .views import (
    FelonysListView,
    FelonysCreateView,
    FelonysDetailView,
    FelonysUpdateView,
)

urlpatterns = [
    path('<int:pk>/edit/',
         FelonysUpdateView.as_view(),
         name='felonys_edit'),
    path('<int:pk>/',
         FelonysDetailView.as_view(),
         name='felonys_detail'),
    path('new/<int:prisoner_pk>/',
         FelonysCreateView.as_view(),
         name='felonys_new'),
    path('',
         FelonysListView.as_view(),
         name='felonys_list'),
]
