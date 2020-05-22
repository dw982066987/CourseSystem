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
            break


@common.auth("student")
def choice_school():
    while True:
        # 获取所有学校
        flag, msg = common_interface.get_all_school_interface()
        if not flag:
            print(msg)
            break
        for index, school_name in enumerate(msg):
            print(f"编号{index},学校名{school_name}")
        choice = input("请输入学校编号:").strip()
        if not choice.isdigit():
            print("请输入数字编号!")
            continue
        choice = int(choice)
        if choice not in range(len(msg)):
            print("输入有误!")
            continue
        school_name = msg[choice]
        flag, msg = student_interface.add_school_interface(school_name, student_info.get("user"))
        if flag:
            print(msg)
            break
        else:
            print(msg)
            break


@common.auth("student")
def choice_course():
    while True:
        # 获取当前学生所在学校的课程列表
        flag, msg = student_interface.get_course_list_interface(student_info.get("user"))
        # 让学生选择课程
        if not flag:
            print(msg)
            break
        for index, course_name in enumerate(msg):
            print(f"编号为{index},课程名{course_name}")
        choice = input("请输入课程编号：").strip()
        if not choice.isdigit():
            print("输入有误！")
            continue
        choice = int(choice)
        if choice not in range(len(msg)):
            print("请输入正确编号！")
            continue
        course_name = msg[choice]
        #  调用选择课程接口
        flag, msg = student_interface.add_course_interface(course_name, student_info.get("user"))
        if flag:
            print(msg)
            break
        else:
            print(msg)
            break


@common.auth("student")
def check_score():
    score = student_interface.check_course_interface(student_info.get("user"))
    if not score:
        print("没有选择则课程！")
    print(score)


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
