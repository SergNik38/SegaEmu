from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.GameListView.as_view(), name='index'),
    path('game/<int:pk>/', views.GameDetailView.as_view(), name='game_detail'),
]
