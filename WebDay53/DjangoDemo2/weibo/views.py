from django.shortcuts import render,redirect


# Create your views here.
def login(req):
    if req.method=="POST":
        if True:
            name = 'jerry'
            # return  render(req,'home.html',locals())  #页面跳转 地址栏不会变化
            return redirect('/home')  #页面跳转 地址栏会变化
    return render(req,'login.html')

def home(req):
    return render(req,'home.html')
