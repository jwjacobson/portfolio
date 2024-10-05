from django.urls import path
from portfolio import views

# app_name = ""

urlpatterns = [
    path("", views.index, name="index"),
    path('<int:pk>/', views.details, name="details")
]