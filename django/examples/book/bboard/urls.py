from django.urls import path
from .views import (
    index, BbCreateView, BbDetailView, BbByRybricView, BbEditView
)


urlpatterns = [
    path('add/', BbCreateView.as_view(), name='add'),
    path('detail/<int:pk>/', BbDetailView.as_view(), name='detail'),
    path('list/<int:pk>/', BbByRybricView.as_view(), name='by_rubric'),
    path('update/<int:pk>/', BbEditView.as_view(), name='edit_bb'),
    path('', index, name='index'),
]
