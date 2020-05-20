"""保存对象与获取对象"""
import os
import pickle
from conf import settings


# 保存数据
def save_data(obj):
    # 获取对象的保存文件夹路径，以类名当作文件夹的名字
    # obj.__class__：获取当前对象的类
    # obj.__class__.__name__：获取类的名字
    class_name = obj.__class__.__name__
    user_dir_path = os.path.join(
        settings.DB_PATH, class_name
    )

    # 判断文件夹是否存在
    if not os.path.exists(user_dir_path):
        os.mkdir(user_dir_path)

    # 拼接当前用户的pickle文件路径，以用户作为文件名
    # obj.username：当前用户的名字
    user_path = os.path.join(
        user_dir_path, obj.username
    )

    # 打开文件保存对象
    with open(user_path, "wb") as f:
        pickle.dump(obj, f)


# 查看数据
# 类，username
def select_data(cls, username):
    # cls.__name__：获取类名
    class_name = cls.__name__
    user_dir_path = os.path.join(
        settings.DB_PATH, class_name
    )
    #
    # 判断文件夹是否存在
    if not os.path.exists(user_dir_path):
        os.mkdir(user_dir_path)

    # 拼接当前用户的pickle文件路径，以用户作为文件名
    # obj.username：当前用户的名字
    user_path = os.path.join(
        user_dir_path, username
    )

    # 判断文件是否存在
    if os.path.exists(user_path):
        # 获取文件对象
        with open(user_path, "rb") as f:
            obj = pickle.load(f)
        return obj
