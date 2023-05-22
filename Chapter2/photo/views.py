from django.shortcuts import render, get_object_or_404, redirect
from .models import Photo
from .forms import PhotoForm

# Create your views here.
def photo_list(request):
    photos = Photo.objects.all()
    # render를 사용해서 photo/photo_list.html을 렌더링, {보낼 데이터이름 : 보낼 데이터}
    return render(request, 'photo/photo_list.html', {'photos': photos})

def photo_detail(request, pk):
    # pk = primary key
    # model로 부터 데이터를 찾고, 없으면 404를 반환하는 함수
    photo = get_object_or_404(Photo, pk=pk)
    return render(request, 'photo/photo_detail.html', {'photo' : photo})

# Post 요청(form작성 전달)일 때, 데이터를 저장하는 함수
def photo_post(request):
    # request의 메소드 타입이 post인 경우
    if request.method == "POST" :
        # PhotoForm에서 post로 보내지는 요청을 form에 담음
        form = PhotoForm(request.POST)
        # form에 작성된 데이터를 검사
        if form.is_valid():
            photo = form.save(commit=False)
            # 잘 작성된 경우, .save()로 데이터를 저장
            photo.save()
            # photo_detail(게시글 상세보기)로 redirect시킴.
            return redirect('photo_detail', pk=photo.pk)
    else:
        form = PhotoForm()
        # 빈 PhotoForm()을 전달해서 form에서 데이터를 입력받을 수 있도록
    return render(request, 'photo/photo_post.html', {'form' : form})

def photo_edit(request, pk) :
    # 요청, 고유번호를 받아서 object를 찾음
    photo = get_object_or_404(Photo, pk=pk)
    # post로 요청이 들어왔을 경우.(수정완료, 수정된 데이터 전달)
    if request.method == "POST":
        # photoform에 instance를 photo로 전달
        form = PhotoForm(request.POST, instance=photo)
        # form이 작성이 잘 되었는지 확인
        if form.is_valid():
            # photo에 form을 save하고
            photo = form.save(commit=False)
            # photo객체를 저장
            photo.save()
            # 상세보기로 redirect
            return redirect('photo_detail', pk=photo.pk)
    else:     # post 요청이 아닐 경우(수정하기, 이전 데이터 전달)
        # photo 객체를 form
        form = PhotoForm(instance=photo)
        # rendering한 후 form전달
    return render(request, 'photo/photo_post.html', {'form':form})