from django.urls import path
from .views import (
    BbCreateView, BbDetailView, BbByRybricView, BbUpdateView,
    BbListView, BbDeleteView, rubrics
)


urlpatterns = [
    path('create/', BbCreateView.as_view(), name='add'),
    path('detail/<int:pk>/', BbDetailView.as_view(), name='detail'),
    path('', BbListView.as_view(), name='bb_list_url'),
    path('bb_by_rubric/<int:pk>/', BbByRybricView.as_view(), name='by_rubric'),
    path('update/<int:pk>/', BbUpdateView.as_view(), name='edit_bb'),
    path('delete/<int:pk>/', BbDeleteView.as_view(), name='bb_delete_url'),
    path('rubrics/', rubrics, name='rubrics_url'),
]
