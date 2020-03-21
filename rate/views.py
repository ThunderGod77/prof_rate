from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Professors,Courses,Employee,Prof_to_subj,ProfRating,ProfReview
from django.contrib.auth.models import User, auth
from .forms import LoginForm
from django.db.models import Avg
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

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        id_=request.POST['id']
        department=request.POST['department']
        img_src=request.POST['img_src']
        password=request.POST['password']
        password_repeat=request.POST['password1']
        if password != password_repeat :
            messages.info(request, 'password not same')
            return redirect('registration')
        user=User.objects.create_user(username=username,password=password_repeat,first_name=firstname,last_name=lastname,)
        user.save()
        employee=Employee.objects.create(user=user,id=id_,user_photo=img_src,department=department)
        employee.save()
        return redirect('login')
    else :
        return render(request,'rate/register.html')
        
def logout(request):
    auth.logout(request) 
    return redirect('/')      




def index(request):
    return render(request, 'rate/index.html')

def prof(request):
    all_prof=Professors.objects.all()
    a=[]
    for prof in all_prof:
        a.append(prof)
    return render(request, 'rate/profInfo.html',{'a':a})

def course(request,):
    course_info=Courses.objects.all()
    a=[]
    for prof in course_info:
        a.append(prof)
    
    return render(request, 'rate/course.html',{'a':a})

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
        

def detail(request,prof_name):
    user=request.user
    if request.method=='POST':
        one=request.POST['1']
        two=request.POST['2']
        three=request.POST['3']
        four=request.POST['4']
        five=request.POST['5']
        six=request.POST['6']
        print(six)

        check=ProfRating.objects.filter(prof_own__prof_name=prof_name,user__username=user.username)
        if check:
            '''print(check[0])
            check[0]['prof_grading_own']=one
            print(check[0])
            check[0].prof_puntuality_own=two
            check[0].prof_strictness_rating_own=three
            check[0].prof_teaching_skill_own=four
            check[0].prof_enthusiasm_own=five
            check[0].prof_overall_own=six
            print("laugh")
            check[0].save()
            print(check[0].prof_grading_own)'''
            prof_own=check[0].prof_own
            check[0].delete()
            rating=ProfRating.objects.create(user=user,prof_own=prof_own,prof_grading_own=one,prof_puntuality_own=two,prof_strictness_rating_own=three,prof_teaching_skill_own=four,prof_enthusiasm_own=five,prof_overall_own=six)
            rating.save()
        else:
            prof_own=Professors.objects.get(prof_name=prof_name)
            rating=ProfRating.objects.create(user=user,prof_own=prof_own,prof_grading_own=one,prof_puntuality_own=two,prof_strictness_rating_own=three,prof_teaching_skill_own=four,prof_enthusiasm_own=five,prof_overall_own=six)
            rating.save()
        return redirect('detail',prof_name=prof_name)
    else:
        prof=Professors.objects.get(prof_name=prof_name)
        subject=Prof_to_subj.objects.filter(professor__prof_name=prof_name)
        b=subject
    
        form_boolean=False
        d=ProfRating.objects.filter(prof_own__prof_name=prof_name).aggregate(Avg('prof_grading_own'))
        e=ProfRating.objects.filter(prof_own__prof_name=prof_name).aggregate(Avg('prof_puntuality_own'))
        f=ProfRating.objects.filter(prof_own__prof_name=prof_name).aggregate(Avg('prof_grading_own'))
        g=ProfRating.objects.filter(prof_own__prof_name=prof_name).aggregate(Avg('prof_strictness_rating_own'))
        h=ProfRating.objects.filter(prof_own__prof_name=prof_name).aggregate(Avg('prof_teaching_skill_own'))
        i=ProfRating.objects.filter(prof_own__prof_name=prof_name).aggregate(Avg('prof_enthusiasm_own'))
        j=ProfRating.objects.filter(prof_own__prof_name=prof_name).aggregate(Avg('prof_overall_own'))
        
        cond=None
        if user is not None :
            cond=ProfRating.objects.filter(prof_own__prof_name=prof_name,user__username=user.username)
            if cond.exists():
                k=0
            else:
                cond=[None]
            form_boolean=True


            
            


        
        return render(request, 'rate/detail.html',{'a':prof,'b':b,'d':d,'e':e,'f':f,'g':g,'h':h,'i':i,'j':j,'cond':cond[0]})
