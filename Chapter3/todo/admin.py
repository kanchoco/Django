from django.contrib import admin
# models에서 Todo를 가져옴
from .models import Todo
# Register your models here.
# 관리자페이지에 Todo모델을 등록
admin.site.register(Todo)