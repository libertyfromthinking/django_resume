from django.urls import path
from .views import *

app_name = 'board'

urlpatterns = [
    path('', BoardLV.as_view(), name='list'),
    path('like/', board_like, name='board_like'),
    path('access_deny/', BoardRedirectView.as_view(), name='deny'), 
    path('add/', BoardCreateView.as_view(), name='add'),
    path('search/', SearchFormView.as_view(), name='search'),
    path('<str:slug>/', BoardDV.as_view(), name='detail'),
    path('<str:slug>/update/', BoardUpdateView.as_view(), name='update'),
    path('<str:slug>/delete/', BoardDeleteView.as_view(), name='delete'),
    path('comment/<int:pk>/remove/', remove_comment, name='remove_comment'),
    path('like/<str:slug>/', board_like, name='board_like'),
]
