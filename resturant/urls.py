from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('menu/', views.MenuItemsView.as_view()),
    path('bookings/', views.BookingViewSet.as_view()),
]