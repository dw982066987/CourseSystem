"""管理员视图"""
from core import src


def logout():
    print("谢谢使用".center(50, "="))
    exit()


def back_index():
    src.run()


def register():
    pass


def login():
    pass


def create_school():
    pass


def create_couse():
    pass


def create_teacher():
    pass


func_dict = {
    "0": logout,
    "1": register,
    "2": login,
    "3": create_school,
    "4": create_couse,
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
                     4、创建老师
                     5、创建课程
                     6、返回主页
        """)
        print("=" * 53)

        choice = input("请输入功能编号:").strip()

        if choice not in func_dict:
            print("请输入正确编号！")
            continue
        func_dict.get(choice)()