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
