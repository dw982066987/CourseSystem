from db import models


def student_register_interface(username, password):
    student_obj = models.Student.select(username)
    if student_obj:
        return False, "学生用户已存在！"
    student_obj = models.Student(username, password)
    student_obj.save()
    return True, "注册成功！"


# def student_login_interface(username, password):
#     student_obj = models.Student.select(username)
#     if not student_obj:
#         return False, "学生用户不存在，请重新输入！"
#     if password == student_obj.password:
#         return True, "登陆成功！"
#     else:
#         return False, "密码错误，请重新输入！"

def add_school_interface(school_name, student_name):
    student_obj = models.Student.select(student_name)
    if student_obj.school:
        return False, "当前学生已经选择学校!"
    # 若不存在学校,则给调用学生对象中选择学校的方法,实现学生添加学校
    student_obj.add_school(school_name)
    return True, "选择学校成功！"
