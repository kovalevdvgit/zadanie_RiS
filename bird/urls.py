from django.urls import path
from bird.views import create_bird, all_bird, func_view_bird, func_recently_view

urlpatterns = [
    path('create_bird/', create_bird, name='create_bird'),
    path('all_bird/', all_bird.as_view(), name='all_bird'),
    path('view_bird/<int:pk>', func_view_bird, name='view_bird'),
    path('recently_view/', func_recently_view, name='recently_view'),
]