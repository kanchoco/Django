# Django
Django 정리한 레파지토리입니다.

참고) 백엔드를 위한 DJANGO REST FRAMEWORK with 파이썬 - 권태형 

### Django

    1. 파이썬 기반의 웹 풀스택 프레임워크
    2. 다른 프레임워크들에 비해 자유도가 낮다
    3. 기본에 충실한 프레임워크
    4. MTV패턴
    5. 배포가 간단함, 무료
    6. 초보자 친화적
    7. port number 8000


### 개발 환경 세팅

1. 가상 환경 세팅
      - 프로젝트마다 필요한 패키지 버전이 다르기 때문에, 가상환경을 사용한다.
      - 의존성 관리와 같은 이름의 개념
      
2. 터미널 
가상 환경 설정<br>

```bash
python --version					#버전 확인
python -m venv myvenv				#myvenv라는 가상 환경 생성
source myvenv\bin\activate				# myvenv 실행(활성화) (. = source)
```

****window
myvenv\Scripts\activate
------------------------------------------------------

Django를 가상 환경에 설치
pip install django~=3.2.10

프로젝트 생성
django-admin startproject myweb .			# .은 새로운 프로젝트를 만들라는 뜻

python manage.py startapp photo			# photo라는 앱폴더를 생성

python manage.py runserver				# 서버를 돌림

*Django의 기본 포트 번호는 8000
*장고의 실행을 멈추고 터미널로 돌아가려면 터미널에서 Ctrl + C를 입력하면된다.

3. 설정 마무리
프로젝트 파일 내 setting.py
------------------------------------------------------
INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'photo',				# 만든 앱 추가
	]
TIME_ZONE = 'Asia/Seoul'			# 시간대 설정
------------------------------------------------------

migration 에러 수정
python manage.py migrate
===================================
Django 프로젝트 구조

프로젝트
	> 하나의 큰 서비스
앱
	> 서비스 내 기능과 같은 요소를 일정한 기준으로 나눠 놓은 단위

===================================
Django 프로젝트 구성요소

manage.py
	- Django관련 명령어를 써야할 때 사용하는 파일
	- django.core.management 모듈로부터 execute_from_command_line 함수를 가져와 
	   입력받은 명령어를 처리한다.

프로젝트 폴더
	- startproject 명령어로 만들어진 폴더, 프로젝트의 설정 및 기본적인 기능 존재
	- 5개의 .py파일 존재
	- settings.py > 설정 파일로 여러 옵션 설정 가능
	- urls.py > 프로젝트 url 주소를 등록해놓는 파일

===================================
MTV 패턴

1. Model - 앱의 데이터와 관련된 부분
- 데이터베이스에 저장될 데이터의 모양을 정의하고 관련된 일부 기능들을 설정해 주는 영역

Django 모델 만들기

model.py에 모델 클래스 만들기

-------------------------------------------
필드종류
CharField : 문자열(길이제한 필요)
IntegerField : 정수
TextField : 문자열(길이제한 필요 없음)
DateField : 날짜
DateTimeField : 날짜 + 시간
FieField : 파일
ImageField : 이미지 파일
ForeignKey : 외래 키(관계)
OneToOneField : 1대 1 관계
ManyToManyField : 다대다 관계
-------------------------------------------

*마이그레이션
- 모델을 데이터베이스에 적용시키는 과정
--------------------------
1. makemigrations : 우리가 모델을 변경한 내용을 기록하여 파일로 만들어주는 과정
2. migrate : makemigrations에서 생성된 파일을 실제로 실행시켜 실제 데이터베이스에 변경 사항을 적용시켜주는 과정
--------------------------

마이그레이션 적용
python manage.py makemigrations

+생성된 모델은 페이지에 적용시켜야한다.
	-------------
from .models import (Class)
admin.site.register(Class)
	------------



2. Templet - 사용자에게 보여지는 부분
- 웹 페이지의 골격, HTML로 작성된 부분
- Django의 템플릿 태그 - 자바스크립트의 역할을함(데이터 주고받기)

3. View - 그 사이에서 데이터를 전달, 이벤트를 처리하는 부분
- 프론트에서의 데이터 요청을 받아서, 데이터를 전달

1) 함수형 뷰

2) 클래스형 뷰

4. Django URL
- 라우팅의 역할, 서버로 해당 주소에 할당된 리소스를 요형하는 역할

=================================
작업 순서
모델 -> 템플릿 -> 뷰 -> URL

1. 모델로 데이터 클래스 생성
2. 템플릿 생성
3. 뷰에 템플릿과 데이터를 주고받을 함수 생성
4. urls에 뷰 추가
=================================

