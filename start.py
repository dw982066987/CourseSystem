"""启动文件入口"""

import sys
import os
from core import src
# 添加根目录至解释器的环境变量中
sys.path.append(
    os.path.dirname(__file__)
)

# 导入主视图
if __name__ == '__main__':
    src.run()