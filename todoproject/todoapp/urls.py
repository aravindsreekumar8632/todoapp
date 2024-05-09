from . import views
from django.urls import path

urlpatterns = [
    path("", views.add, name='addTask'),
    path("delete/<int:taskid>/", views.delete, name='deleteTask'),
    path("update/<int:id>", views.update, name='updateTask'),
]