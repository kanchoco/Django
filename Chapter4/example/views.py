from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from .models import Book
from .serializer import BookSerializer

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