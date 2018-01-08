from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
import datetime
from blog import models
#视图函数将页面进行返回  默认会传一个参数
def shownews(request):
    # return HttpResponse('<h1>ok</h1>') #实例化一个response对象 返回给浏览器
    #返回一个页面调用render方法
    times=datetime.datetime.now()
    #render格式化页面将字符串用变量进行替换 渲染
    #render(参数1 request,'页面','替换变量') 将request返回到页面 前台页面也可以调用request对象
    return render(request,'default.html',{"abc":times})

#用户新增页面
Userlist=[]
def Useradd(request):
    #获取请求数据
    if request.method=="POST":
        #获取数据 没有值返回None
        name=request.POST.get('name',None)
        email=request.POST.get('email',None)
        mobile=request.POST.get('mobile',None)
        address=request.POST.get('address',None)
        # User={"name":name,'email':email,'mobile':mobile,"address":address}
        # Userlist.append(User)
        #存入数据库
        models.User.objects.create(
            name=name,
            email=email,
            mobile=mobile,
            address=address,
        )
        #展示数据
        Userlist=models.User.objects.all()
        print(Userlist)
        return  render(request,'Useradd.html',{'User_list':Userlist}) #替换占位符

    return render(request,'Useradd.html')


def viewcust(req):
    return HttpResponse('2003')

#参数取值
def index(req,name):
    return HttpResponse(name)

def index2(request):
    if request.method == "POST":
        name = request.POST.get('name', None)
        pwd = request.POST.get('pwd', None)
        if name=='jerry' and pwd=='123':
            return HttpResponse('登陆成功')
    return render(request,'login.html')


def bmw(request):
    return HttpResponse('<h1>blog下面的BMW</h1>')

#response对象的使用

def login2(request):
    if request.method == "POST":
        name = request.POST.get('name', None)
        pwd = request.POST.get('pwd', None)
        if name == 'jerry' and pwd == '123':
           return redirect('car/bmw')       #redirect跳转页面使用 也是使用路径
    return render(request, 'login.html')

