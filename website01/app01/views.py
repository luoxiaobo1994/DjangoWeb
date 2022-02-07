from django.shortcuts import render, HttpResponse


# Create your views here.


def index(request):  # request是必要的参数,也可以写成req,不是固定的形参.
    # 只是普通的返回一个文本.
    return HttpResponse("首个返回数据")


def user_add(request):
    return render(request,'user_add.html')


def user_list(request):
    # 返回一个html文件时.要返回的是render,第一个返回的参数就是request
    # 找html文件的顺序:
    # 1.如果settings.py里TEMPLATES设置了DIRS:[os.path.join(BASE_DIR)],那么就先到项目根目录里的templates里找.
    # 2.没有设置setting.py的情况下,根据app的注册顺序,一个一个去找.
    return render(request, "user_list.html")
