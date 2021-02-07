from django.urls import path
from shop import views

urlpatterns = [
    path('hello/', views.hello_world),
]
