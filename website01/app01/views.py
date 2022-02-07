from django.shortcuts import render, HttpResponse, redirect


# Create your views here.


def index(request):  # request是必要的参数,也可以写成req,不是固定的形参.
    # 只是普通的返回一个文本.
    return HttpResponse("首个返回数据")


def user_add(request):
    return render(request, 'user_add.html')


def user_list(request):
    # 返回一个html文件时.要返回的是render,第一个返回的参数就是request
    # 找html文件的顺序:
    # 1.如果settings.py里TEMPLATES设置了DIRS:[os.path.join(BASE_DIR)],那么就先到项目根目录里的templates里找.
    # 2.没有设置setting.py的情况下,根据app的注册顺序,一个一个去找.
    return render(request, "user_list.html")


def something(request):
    # request 是一个对象,封装了用户发送过来的请求相关数据
    print(request.method)  # 获取用户的请求方式.
    print(f"获取到的参数:{request.GET}")  # 获取用户输入的参数.获取到的参数:<QueryDict: {'n1': ['1000']}>

    # 3.[响应] 返回内容字符串
    # return HttpResponse("返回内容")

    # 4.[响应] 读取HTML的内容 + 渲染(替换)  --> 生成新的字符串,返回给用户的浏览器.
    # return render(request,"something.html",{"title":"来了"})

    # 5.[响应] 重定向
    return redirect("https://www.baidu.com")


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    # 如果是post请求,则获取用户提交的数据
    username = request.POST.get("user")
    password = request.POST.get("pwd")
    if username == 'root' and password == '123':
        # return HttpResponse("登录成功")
        return redirect("https://www.baidu.com")
    return render(request, "login.html", {"error_msg": "用户名或密码错误"})
