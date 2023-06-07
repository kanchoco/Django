from django.urls import path
from .views import TodosAPIMixins

urlpatterns = [
    path('todo/', TodosAPIMixins.as_view()),
]