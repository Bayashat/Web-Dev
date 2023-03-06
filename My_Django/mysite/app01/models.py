from django.db import models
import datetime

"""
在底层, ORM会实现: 
create table app01_userinfo(
    id bigint auto_increment primary key    会自动生成
    username varchar(30),
    password varchar(20),
    age int
    ...
)
"""

class UserInfo(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    age = models.IntegerField(default=2)  
    # gender = models.BooleanField(default=True)
    # date_of_birth = models.DateField(null=True, blank=True)  
    # last_login_time = models.DateField(default=datetime.date.today)  # 默认为空
    # register_time = models.DateField(default=datetime.date.today)
    # is_Admin = models.BooleanField(default=False)

    # def __str__(self):
    #     return f"""
    #     Username is {self.username}, password is {self.password}, age is {self.age}, gender is {self.gender}, 
    #     The date of birth is {self.date_of_birth}, The last login time is {self.last_login_time}, 
    #     The register time is {self.register_time}, is admin {self.is_Admin}"""

class Department(models.Model):
    """ 部门表 """
    title = models.CharField(verbose_name="标题", max_length=32)  # verbose_name 是一个注解或者备注

    def __str__(self):
        return self.title

class Employee_info(models.Model):
    """ 员工表 """
    name = models.CharField(verbose_name="姓名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)
    age = models.IntegerField(verbose_name="年龄")
    
    # 在Django中做约束
    gender_choices = (
            (1, 'Male'),
            (2, 'Female'),
    )
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)

    account = models.DecimalField(verbose_name="账户余额", max_digits=10, decimal_places=2, default=0)

    create_time = models.DateTimeField(verbose_name="入职时间")

    # depart_id = models.BigIntegerField(verbose_name="部门ID")  #  无约束

    # 1. Django在生成后, 会自动加下划线id : depart_id
    # 2. to -> 与哪张表关联, to_field -> 与表中的哪一列关联
    """ 3. 部门表被删的话: 
        3.1 级联删除(on_delete=models.CASCAD)
        3.2 置空: 员工表里, 部门被删了的, 置为空
"""
    depart = models.ForeignKey(verbose_name="部门", to="Department", to_field="id", on_delete=models.CASCADE) 

    # insert into app01_employee_info(name, password, age, account, create_time, gender, depart_id) values('Bayashat', "666", 20, 100.68, "2020-01-11", 1, 1);
    # insert into app01_employee_info(name, password, age, account, create_time, gender, depart_id) values('Kyran', "12574", 22, 999, "2022-08-27", 1, 13);
    # insert into app01_employee_info(name, password, age, account, create_time, gender, depart_id) values('Bakytgul', "qwerty123456", 26, 9999999, "2014-01-01", 2, 14);


class Role(models.Model):
    caption = models.CharField(max_length=16)


#       1. 新建数据 insert into app01_department(title) values("销售部")
# Department.objects.create(title="销售部")
# UserInfo.objects.create(username="Bayashat", password="123456", age=20, date_of_birth="2002-12-23")

#       2. 删除数据
# UserInfo.objects.filter(id=2).delete()  
# Department.objects.all().delete()  