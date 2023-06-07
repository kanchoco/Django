from rest_framework import serializers
from .models import Todo

# 사용 방법에 따라 형태가 다른 시리얼라이저를 만들어야함

#조회용 시리얼라이저
# 전체 조회에서는 Todo 설명을 제외한 제목, 완료여부, 중요 여부가 필요하기 때문에 이들만 포함
class TodoSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'complete', 'important')