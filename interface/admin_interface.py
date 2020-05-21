"""管理员接口"""
from db import models


# 管理员注册接口
def admin_register_interface(username, password):
    # 判断用户是否存在
    # 调用Admin类中的select方法，由该方法调用db_handler中的select_data功能获取对象
    admin_obj = models.Admin.select(username)
    # 若存在，返回用户以存在给视图层
    if admin_obj:
        return False, "用户已存在！"
    # 若不存在，调用类实例化一个对象并保存
    admin_obj = models.Admin(username, password)
    # 对象调用save（）会将admin_obj传给save方法
    admin_obj.save()
    return True, "注册成功"


# 管理员登陆接口
def admin_login_interface(username, password):
    admin_obj = models.Admin.select(username)
    if not admin_obj:
        return False, "用户名不存在！"
    if password == admin_obj.password:
        return True, "登陆成功！"
    else:
        return False, "密码错误，请重新输入！"


# 创建学校接口
def create_school_interface(school_name, school_addr, admin_name):
    school_obj = models.School.select(school_name)
    if school_obj:
        return False, "学校已存在，请重新注册！"
    admin_obj = models.Admin.select(admin_name)
    admin_obj.create_school(
        school_name, school_addr
    )
    return True, "学校创建成功！"


# 创建课程接口
def create_course_interface(school_name, course_name, admin_name):
    # 查看课程是否存在
    # 先获取学校对象中的课程列表
    school_obj = models.School.select(school_name)
    # 判断当前课程是否存在课程列表中
    if course_name in school_obj.course_list:
        return False, "当前课程已存在！"
    # 若课程不存在则由管理员创建课程
    admin_obj = models.Admin.select(admin_name)
    admin_obj.create_course(school_obj, course_name)

    return True, f"{course_name}创建成功，绑定给{school_name}"


# 创建教师接口
def create_teacher_interface(teacher_name, admin_name, teacher_pwd="123"):
    # 判断老师是否存在
    teacher_obj = models.Teacher.select(teacher_name)
    # 若存在，则返回不能创建
    if teacher_obj:
        return False, "老师已存在！"
    # 若不存在，则让管理员创建
    admin_obj = models.Admin.select(admin_name)
    admin_obj.create_teacher(teacher_name, teacher_pwd)
    return True, f"{teacher_name}，创建成功！"
