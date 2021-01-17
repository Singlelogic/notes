from django.urls import path
from .views import (
    # index, by_rubric, BbCreateView, BbDetailView, RubricDetailView
    index, BbCreateView, BbDetailView, RubricDetailView
)


urlpatterns = [
    path('add/', BbCreateView.as_view(), name='add'),
    path('detail/<int:pk>/', BbDetailView.as_view(), name='detail'),
    path('detail_rubric/<int:pk>/', RubricDetailView.as_view(), name='detail_rubric'),
    # path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('', index, name='index'),
]
