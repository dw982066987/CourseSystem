"""公共接口"""
import os
from conf import settings
from db import models


# 获取所有学校名称接口
def get_all_school_interface():
    # 获取学校文件夹路径
    school_dir = os.path.join(
        settings.DB_PATH, "School"
    )

    # 判断文件夹是否存在
    if not os.path.exists(school_dir):
        return False, "没有学校，请先联系管理员！"

    school_list = os.listdir(school_dir)
    return True, school_list


# 公共登陆接口
def login_interface(username, password, user_type):
    if user_type == "admin":
        obj = models.Admin.select(username)
    elif user_type == "student":
        obj = models.Student.select(username)
    elif user_type == "teacher":
        obj = models.Teacher.select(username)
    else:
        return False, "登陆角色错误，请重新输入！"
    if obj:
        if password == obj.password:
            return True, "登陆成功！"
        else:
            return False, "密码错误,请重新输入！"
    else:
        return False, "用户名不存在，请重新输入"

