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
