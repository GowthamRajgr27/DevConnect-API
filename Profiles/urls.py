from django.urls import path
from .views import ProfileCreateView, ProfileDetailView, ConnectView

urlpatterns = [
    path('', ProfileCreateView.as_view()),
    path('<int:pk>/', ProfileDetailView.as_view()),
    path('connect/<int:pk>/', ConnectView.as_view()),
]
