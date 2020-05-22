from db import models


def student_register_interface(username, password):
    student_obj = models.Student.select(username)
    if student_obj:
        return False, "学生用户已存在！"
    student_obj = models.Student(username, password)
    student_obj.save()
    return True, "注册成功！"
