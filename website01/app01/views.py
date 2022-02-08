from django.shortcuts import render, HttpResponse, redirect
import requests
from app01.models import UserInfo,Department

# Create your views here.

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"
}


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


def tpl(request):
    name = "炬星"
    robot = {"小白龙": "雷龙", "小旋风": "梁龙"}
    list_info = ['列表元素1', '列表元素2', '列表元素3']
    data_list = [
        {"name": "刘备", "salary": "100000", "role": "大哥"},
        {"name": "关羽", "salary": "98000", "role": "二哥"},
        {"name": "张飞", "salary": "97500", "role": "三弟"}
    ]
    return render(request, 'tpl.html', {"n1": name, "n2": robot, "n3": list_info, "n4": data_list})


def news(req):
    # 通过爬虫去获取别人的新闻
    res = requests.get("http://www.chinaunicom.com.cn/api/article/NewsByIndex/1/2021/11/news", headers=headers)
    data = res.json()
    # data = {}
    print(data)
    return render(req, "news.html", {"news": data})


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


def orm(request):
    # 测试orm能否获取到数据库中的数据.
    """      新建数据      """
    # Department.objects.create(title="市场部")
    # Department.objects.create(title="测试部")
    # Department.objects.create(title="软件研发部")
    # Department.objects.create(title="硬件研发部")
    # UserInfo.objects.create(name="root",password="123456",age=18)
    # UserInfo.objects.create(name="admin",password="admin123",age=28)
    # UserInfo.objects.create(name="luoxiaobo",password="lxb123",age=28)

    """       删除数据     """  # 删除之前一定是先筛选出来要删的.
    # UserInfo.objects.filter(id=3).delete()  # 删除id=3的行
    # Department.objects.all().delete()  # 清空整个表.

    """       数据获取     """
    # data_list = UserInfo.objects.all()  # 得到一个列表(QuerySet类型,不是list),也不是实际数据,而是对象.
    # for obj in data_list:  # 循环遍历对象.
    #     print('获取到的数据:',obj.id,obj.name,obj.password,obj.age) # 拿到对象的数据.
    # print(data_list)

    # 只拿一行的情况
    # row_obj = UserInfo.objects.filter(id=1).first()  # filter拿到的也是一个列表.first则是这个列表的第一个.
    # print(row_obj.id,row_obj.name,row_obj.password,row_obj.age)

    # """       更新数据      """
    # UserInfo.objects.filter(id=2).update(age=31)


    return HttpResponse("操作成功")

def info_list(request):
    # 1.获取数据库中所有的用户信息.
    data_list = UserInfo.objects.all()  # 对象列表.
    return render(request,'info_list.html',{"data_list":data_list})

def info_add(request):
    # 添加用户
    if request.method == "GET":
        return render(request,'info_add.html')
    # 获取前端提交的数据
    user = request.POST.get("user")
    pwd = request.POST.get("pwd")
    age = request.POST.get("age")
    # 添加到数据库
    UserInfo.objects.create(name=user,password=pwd,age=age)
    return redirect("/info/list")
