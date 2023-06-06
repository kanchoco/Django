# 기본형 뷰 
from rest_framework import permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from .models import Book
from .serializer import BookSerializer
# 믹싱, 제네릭
from rest_framework import generics  
from rest_framework import mixins
# Viewset
from rest_framework import viewsets

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer = BookSerializer

# 목록과 수정
class BooksAPIGenerics(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

#업데이트와 삭제 
class BookAPIGenerics(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'bid'

# ------------
class BooksAPIMixins(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    # 받아온 데이터
    queryset = Book.objects.all()
    # 사용할 시리얼라이저
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):            #GET 메소드 처리 함수(전체 목록)
        return self.list(request, *args, **kwargs)      #mixins.ListModelMixin 과 연결
    def post(self, request, *args, **kwargs):           #POST 메소드 처리 함수(1권 등록)
        return self.create(request, *args, **kwargs)    #mixins.CreateModelMixin과 연결

class BookAPIMixins(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'bid'
    # Django 기본 모델 pk가 아닌 bid를 pk로 사용하고 있으니 lookup_field로 설정

    def get(self, request, *args, **kwargs):            # GET 메소드 처리 함수(1권 정보)
        return self.retrieve(request, *args, **kwargs)  # mixins.RetrieveModelMixin과 연결
    def put(self, request, *args, **kwargs):            # PUT 메소드 처리 함수(1권 정보 수정)
        return self.update(request, *args, **kwargs)    # mixins.UpdateModelMixin과 연결
    def delete(self, request, *args, **kwargs):         # DELETE 메소드 처리(1권 정보 삭제)
        return self.destroy(request, *args, **kwargs)    # mixins.DeleteModelMixin과 연결

# 함수형 뷰
@api_view(['GET'])
def HelloAPI(request) :
    return Response("Hello world!")

@api_view(['GET', 'POST'])
def booksAPI(request) :
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        # 시리얼라이저에 전체 데이터를 한번에 집어넣음(직렬화, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) #200-GET요청이 정상적으로 이루어진 상태
    elif request.method == 'POST' :
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid() : #유효한 데이터인지
            serializer.save() #역직렬화를 통해 데이터 저장
            return Response(serializer.data, status=status.HTTP_201_CREATED) #201-POST요청이 정상적으로 이루어진 상태
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def bookAPI(request, bid) :
    book = get_object_or_404(Book, bid=bid) #bid존재하면 가져오고 아니면 400에러 반환
    serializer = BookSerializer(book) #시리얼라이저에 데이터를 넣음, 직렬화
    return Response(serializer.data, status=status.HTTP_200_OK)

# 클래스 기반 뷰
# class HelloAPI(APIView) :
#     def get(self, request) :
#         return Response("Hello world!")
class BooksAPI(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) 
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookAPI(APIView):
    def get(self, request, bid):
        book = get_object_or_404(Book, bid=bid)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
        

