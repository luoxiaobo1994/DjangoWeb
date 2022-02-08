from django.db import models

# Create your models here.

class UserInfo(models.Model):  # 类名=表名

    name = models.CharField(max_length=32)  # 字段1,约束
    password = models.CharField(max_length=64)  # 字段2,约束
    age = models.IntegerField()
    """
    会根据上面的字段,去创建一张表.  数据库使用settings.py里配置的去使用.
    执行了以下命令:
    create table app01_userinfo(
        id bigint aoto_increment primary key,
        name varchar(32),
        password varchar(64),
        age int
        )
    
    """


class Department(models.Model):
    title = models.CharField(max_length=32)


# 新建数据: insert into app01_department(title) values("销售部")
# Department.objects.create(title='销售部')
