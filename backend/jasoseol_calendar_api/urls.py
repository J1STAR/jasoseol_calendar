from django.urls import path
from . import views

urlpatterns = [
    path('todo/', views.TodoView.as_view(), name="todo-list"),
    path('todo/<int:year>/<int:month>/', views.TodoMonthView.as_view(), name="month-todo-list"),
    path('todo/<int:year>/<int:month>/<int:date>/', views.TodoDateView.as_view(), name="todo-detail")
]