"""学员视图"""
from core import src
from lib import common
from interface import student_interface
from interface import common_interface

student_info = {
    "user": None
}


def logout():
    print("谢谢使用".center(50, "="))
    exit()


def back_index():
    src.run()


def register():
    while True:
        username = input("请输入用户名：").strip()
        password = input("请输入密码：").strip()
        re_password = input("请确认密码：").strip()
        if re_password == password:
            flag, msg = student_interface.student_register_interface(username, password)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print("用户名或密码错误，请重新输入！")


def login():
    while True:
        username = input("请输入用户名：").strip()
        password = input("请输入密码：").strip()
        # flag, msg = student_interface.student_login_interface(username,password)
        flag, msg = common_interface.login_interface(username, password, user_type="student")
        if flag:
            print(msg)
            student_info["user"] = username
            break
        else:
            print(msg)
            continue


@common.auth("student")
def choice_school():
    pass


@common.auth("student")
def choice_course():
    pass


@common.auth("student")
def check_score():
    pass


func_dict = {
    "0": logout,
    "1": register,
    "2": login,
    "3": choice_school,
    "4": choice_course,
    "5": check_score,
    "6": back_index
}


def student_view():
    # 管理主界面
    while True:
        print("欢迎来到学员界面".center(47, "="))
        print("""
                     0、退出
                     1、注册
                     2、登录
                     3、选择校区
                     4、选择课程
                     5、查看成绩    
                     6、返回主页          
         """)
        print("=" * 53)

        choice = input("请输入功能编号：").strip()

        if choice not in func_dict:
            print("请输入正确编号！")
            continue
        func_dict.get(choice)()
