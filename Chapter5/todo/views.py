# 믹싱, 제네릭
from rest_framework import generics , status, permissions
from rest_framework import mixins
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import TodoSimpleSerializer, TodoDetailSerializer, TodoCreateSerializer
from .models import Todo

# 실습 목표 mixin, fbc, cbv 작성에 익숙해지기

# 전체 조회(미완료)
# create와 list의 시리얼라이저가 다른 상황, 하나의 클래스에 선언하고 싶어서 기본 cbv로 바꾸었다.
class TodosAPIView(APIView):
    # 완료하지 않은 항목만 나오도록 필터링
    def get(self, request):        #GET 메소드 처리 함수(전체 목록)
        todos = Todo.objects.filter(complete=False)
        serializer = TodoSimpleSerializer(todos, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    def post(self, request):
        serializer = TodoCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

# 전체 조회(완료), 상세 조회(완료 수정)
# API는 pk 필요 여부에 따라 주소가 다르기 때문에 각각 하나의 클래스로 작성한다.
# 나는 mixin을 사용하면서 detailserializer로 수정에서 완료여부를 바꿀 수 있지만, 교재에서는 createSerializer를 사용해서 완료여부가 수정이 불가능하다
# 그래서 기능적으로 구현할 필요성은 없지만 실습을 위해서 완료여부 수정 기능도 작성한다.!
class DoneTodosAPIView(APIView):
    def get(self, request):
        dones = Todo.objects.filter(complete=True)
        serializer = TodoSimpleSerializer(dones, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class DoneTodoAPIView(APIView):
    def get(self, request, pk) :
        done = get_object_or_404(Todo, id=pk)
        # 완료여부 수정
        done.complete = True
        # 저장
        done.save()
        # 직렬화
        serializer = TodoDetailSerializer(done)
        return Response(status=status.HTTP_200_OK)



# 상세 조회, 수정 믹싱
class TodoAPIMixins(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoDetailSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

