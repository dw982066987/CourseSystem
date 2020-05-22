"""管理员视图"""
from core import src
from interface import admin_interface
from interface import common_interface
from lib import common

admin_info = {
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
            # 调用管理员接口层
            flag, msg = admin_interface.admin_register_interface(username, password)
            if flag:
                print(msg)
                break
            else:
                print(msg)
                break
        else:
            print("用户名或密码错误，请重新输入！")
            continue


def login():
    while True:
        username = input("请输入用户名：").strip()
        password = input("请输入密码：").strip()
        # flag, msg = admin_interface.admin_login_interface(username, password)
        flag, msg = admin_interface.common_interface.login_interface(username, password, user_type="admin")
        if flag:
            print(msg)
            # 记录当前操作
            admin_info["user"] = username
            break
        else:
            print(msg)
            continue


@common.auth("admin")
def create_school():
    while True:
        school_name = input("请输入要创建的学校名字：").strip()
        school_addr = input("请输入要创建的学校地址：").strip()
        flag, msg = admin_interface.create_school_interface(
            school_name, school_addr, admin_info.get("user")
        )
        if flag:
            print(msg)
            break
        else:
            print(msg)
            continue


@common.auth("admin")
def create_course():
    while True:
        # 调用接口获取学校名称
        flag, msg = common_interface.get_all_school_interface()
        if not flag:
            print(msg)
            break
        for index, school_name in enumerate(msg):
            print(f"编号{index},学校名称{school_name}")
        choice = input("请输入学校编号：")
        if not choice.isdigit():
            print("请输入数字！")
            continue
        choice = int(choice)

        if choice not in range(len(msg)):
            print("请输入正确编号！")
            continue

        # 获取选择后的学校名字
        school_name = msg[choice]

        # 选择课程名称
        course_name = input("请输入需要创建的课程名称：").strip()

        # 调用接口层
        flag, msg = admin_interface.create_course_interface(
            # 关联学校和课程
            school_name, course_name, admin_info.get("user")
        )
        if flag:
            print(msg)
            break
        else:
            print(msg)
            continue


@common.auth("admin")
def create_teacher():
    while True:
        teacher_name = input("请输入老师的名字：").strip()
        # 调用接口创建老师
        flag, msg = admin_interface.create_teacher_interface(
            teacher_name, admin_info.get("user")
        )
        if flag:
            print(msg)
            break
        else:
            print(msg)
            break


func_dict = {
    "0": logout,
    "1": register,
    "2": login,
    "3": create_school,
    "4": create_course,
    "5": create_teacher,
    "6": back_index
}


def admin_view():
    # 管理主界面
    while True:
        print("欢迎来到管理员界面".center(47, "="))
        print("""
                     0、退出
                     1、注册
                     2、登录
                     3、创建学校
                     4、创建课程
                     5、创建老师
                     6、返回主页
        """)
        print("=" * 53)

        choice = input("请输入功能编号:").strip()

        if choice not in func_dict:
            print("请输入正确编号！")
            continue
        func_dict.get(choice)()
