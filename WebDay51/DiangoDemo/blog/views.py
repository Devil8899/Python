from django.shortcuts import render,HttpResponse

# Create your views here.
import datetime
from blog import models
#视图函数将页面进行返回  默认会传一个参数
def shownews(request):
    # return HttpResponse('<h1>ok</h1>') #实例化一个response对象 返回给浏览器
    #返回一个页面调用render方法
    times=datetime.datetime.now()
    #格式化页面将字符串用变量进行替换 渲染
    #render(参数1 request,'页面','替换变量') 将request返回到页面 前台页面也可以调用request对象
    return render(request,'default.html',{"abc":times})

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