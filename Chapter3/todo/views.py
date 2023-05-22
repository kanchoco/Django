from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

# Create your views here.
# Todo 데이터를 템플릿으로 전달, 전체조회에서는 완료되지 않은 데이터만 전달할 것이므로 complete요소의 값이 false인 경우만 전달한다.
def todo_list(request):
    todos = Todo.objects.filter(complete = False)
    return render(request, 'todo/todo_list.html', {'todos' : todos})

# Todo 데이터를 템플릿으로 전달, 상세보기에서는 전달받은 pk에 해당하는 todo를 전달한다
def todo_detail(request, pk):
    todo = Todo.objects.get(id=pk)
    return render(request, 'todo/todo_detail.html', {'todo' : todo})

# form태그로 전달받은 데이터를 가공
def todo_post(request) :
    # 입력페이지가 요청되는 경우는? 두가지이다.
    # GET으로 요청 - 작성페이지
    # POST로 요청 - 작성완료
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            # redirect는 임포트해서 사용하는것.. 기본제공아님
            return redirect('todo_list')
    else :
        form = TodoForm()
        # 폼의 값이 유효하지 않을 때, GET방식일때 리턴
    return render(request, 'todo/todo_post.html', {'form' : form})

    # 수정은 생성과 기능이 유사함으로, 따로 템플릿을 생성하지 않고 뷰와 url만 생성함
    # 수정한 객체를 알아야하므로 pk전달
def todo_edit(request, pk) :
    todo = Todo.objects.get(id=pk)
    if request.method == "POST" :
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid() :
            todo = form.save(commit = False)
            todo.save()
            return redirect('todo_list')
        else :
            form = TodoForm()
    return render(request, 'todo/todo_post.html', {'form' : form})

def todo_done_list(request) :
    todos = Todo.objects.filter(complete = True)
    return render(request, 'todo/todo_list.html', {'todos' : todos})

def todo_done(request, pk) :
    todo = Todo.objects.get(id = pk)
    todo.complete = True
    todo.save()
    return redirect('todo_done_list')