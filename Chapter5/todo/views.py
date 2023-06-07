# 믹싱, 제네릭
from rest_framework import generics  
from rest_framework import mixins

from .serializers import TodoSimpleSerializer
from .models import Todo

class TodosAPIMixins(mixins.ListModelMixin, generics.GenericAPIView):
    # 완료하지 않은 항목만 나오도록 필터링
    queryset = Todo.objects.filter(complete=False)
    serializer_class = TodoSimpleSerializer

    def get(self, request, *args, **kwargs):        #GET 메소드 처리 함수(전체 목록)
        return self.list(request, *args, **kwargs)  #mixins.ListModelMixin 과 연결


