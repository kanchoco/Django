from rest_framework import serializers
from .models import Todo

# 사용 방법에 따라 형태가 다른 시리얼라이저를 만들어야함

#조회용 시리얼라이저
# 전체 조회에서는 Todo 설명을 제외한 제목, 완료여부, 중요 여부가 필요하기 때문에 이들만 포함
class TodoSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        # '__all__'
        fields = ('id', 'title', 'complete', 'important')

# 상세조회용 시리얼라이저
# 상세조회에서는 내용이 필요해지므로 필드에 description을 추가한다.
class TodoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'complete', 'important')

# 생성용 시리얼라이저
class TodoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('title', 'description', 'important')
