from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from .models import tb_news
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
# def index(request, fname, lname, age, hobby):
#     # return HttpResponse("Hello Django")
#     data ={
#         'fname' : fname,
#         'lname' : lname,
#         'age'   : age,
#         'hobby' : hobby
#     }
#     return render(request, 'myWebsite/index.html', data)

def index(request):
    content = tb_news.objects.all().order_by("-id")
    data ={
        'news' : content,

    }
    return render(request, 'myWebsite/index.html', data)
    

def showName(request, fname,lname):
    return HttpResponse("My name is "+ fname +" "+ lname)

@login_required(login_url='/loginUser')
def addNews(request):
    return render(request, 'myWebsite/addNews.html')

def recordNews(request):
    toppic = request.POST['toppic_news']
    detail = request.POST['detail_news']
    photo = request.FILES['photo_news']
    content = tb_news( toppic_news=toppic, detail_news=detail, photo_news=photo)
    content.save()
    return redirect('/contentNews')

@login_required(login_url='/loginUser')
@permission_required('is_saff', login_url='/loginWarning')
def contentNews(request):
    content = tb_news.objects.all()
    data ={
        'content' : content
    }
    return render(request, 'myWebsite/contentNews.html', data)

def contentEdit(request):
    id = request.GET['id']
    result = tb_news.objects.filter(pk=id)
    data = {
        'result' : result   
    }
    return render(request, 'myWebsite/contentEdit.html', data)


def contentUpdate(request):
    id = request.POST['id']
    topic = request.POST['toppic_news']
    detail = request.POST['detail_news']
    photo = request.FILES['photo_news']

    content = tb_news.objects.get(pk=id)
    content.toppic_news = topic
    content.detail_news = detail
    content.photo_news = photo
    content.save()
    return redirect('/contentNews')

def contentDelete(request):
    id = request.GET['id']
    content = tb_news.objects.get(pk=id)
    content.delete()
    return redirect('/contentNews')

def contentShow(request):
    id = request.GET['id']
    result = tb_news.objects.filter(pk=id)
    data = {
        'result' : result,
    }
    return render(request,'myWebsite/contentShow.html',data)

def registUser(request):
    return render(request,'myWebsite/registUser.html')

def registData(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    username = request.POST['username']
    password = request.POST['password']
    repassword = request.POST['repassword']
    
    if password == repassword:
        if User.objects.filter(username = username).exists():
            messages.error(request,'Username has been already usend')
            return redirect('/registUser')
            # messages.error(request)
            # return HttpResponse('Username has been already usend')
        elif User.objects.filter(email = email).exists():
            messages.error(request,'Email has been already used')
            return redirect('/registUser')
            # return HttpResponse('Email has been already used')
        else:
            user = User.objects.create_user(
            first_name = fname,
            last_name = lname,
            username = username,
            password = password,
            email = email
        ) 
        user.save()
        return HttpResponse("Data saved")
    else:
            messages.error(request,'Password is not equal to re-password')
            return redirect('/registUser') 
            # return HttpResponse('') 
        
def loginUser(request):
    if request.user.is_authenticated:
        return redirect('/')
    return render(request, 'myWebsite/loginUser.html') 

def loginData(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return redirect('/')
    else:
        messages.error(request, 'Login error')
        return redirect('/loginUser')
    
def logoutUser(request):
    auth.logout(request)
    return redirect('/loginUser')
    
def loginWarning(request):
    return render(request,'myWebsite/loginWarning.html')


def handler404(request, exception):
    return render(request,'myWebsite/404errorPage.html')
# def resultPage(request):
#     # topic = request.POST['topic_news']
#     # detail = request.POST['detail_news']
#     topic = request.GET['topic_news']
#     detail = request.GET['detail_news']

#     data ={

#         'topic' : topic,
#         'detail' : detail,
        
#     }

#     return render(request, 'myWebsite/resultPage.html', data) 
