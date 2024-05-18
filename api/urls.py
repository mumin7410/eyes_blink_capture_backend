from django.urls import path

from . import views

urlpatterns = [
    path('find_emp/', views.receive_image, name='find_emp'),
]