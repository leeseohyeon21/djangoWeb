from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('<str:user_id>/reservation/', views.movieSelect),
    path('<str:user_id>/reservation/<int:movie_id>/', views.screenTimeSelect, name='screenTime'),
    path('<str:user_id>/reservation/<int:movie_id>/<str:screen_id>/', views.seatSelect, name='seat'),
    path('<str:user_id>/reservation/<int:movie_id>/<str:screen_id>/<int:seat_id>/', views.confirm, name='confirm'),
    path('<str:user_id>/myhistory/', views.myhistory),
    path('<str:user_id>/cancel/<str:reservation_id>', views.cancel),
    path('initial/', views.initial),
]
