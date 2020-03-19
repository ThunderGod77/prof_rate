from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Professors,TaughtBy,Courses,Employee
from django.contrib.auth.models import User, auth
from .forms import LoginForm
# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        
        user=auth.authenticate(username=username,password=password)
        if user is not None :
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "invalid credentials")
            return redirect('login')
    else:
        return render(request, 'rate/login.html')






def index(request):
    return render(request, 'rate/index.html')

def prof(request,prof_name="Anant Maji"):
    prof_info=Professors.objects.get(prof_name=prof_name)
    id=prof_info.id
    prof_subj=TaughtBy.objects.filter(prof_name=id)

    return render(request, 'rate/profInfo.html',{'prof_info':prof_info,'prof_subj':prof_subj})

def course(request,course_id="MTL106"):
    course_info=Courses.objects.filter(course_id=course_id).values('course_description')
    jk=course_info[0]["course_description"]
    return render(request, 'rate/course.html',{'course_info':course_info,'jk':jk})

def my_view(request):
    login_data = request.POST.dict()
    username = login_data.get['username']
    password = login_data.get['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'rate/mypage.html',{'user':user})
        
    else:
        return render(request,'rate/course.html')
        
        