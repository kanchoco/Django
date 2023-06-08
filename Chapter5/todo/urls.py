from django.urls import path
from .views import TodosAPIView, TodoAPIMixins, DoneTodoAPIView, DoneTodosAPIView

urlpatterns = [
    path('todo/', TodosAPIView.as_view()),
    path('todo/<int:pk>/', TodoAPIMixins.as_view()),
    path('done/', DoneTodosAPIView.as_view()),
    # 이경로로 요청하면 완료여부가 수정이 된다.
    path('done/<int:pk>/', DoneTodoAPIView.as_view()),
]