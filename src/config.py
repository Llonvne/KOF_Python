"""
config: KOF 关键参数配置目录
"""

# 导入外部资源管理器
import os

import mediaLibraryManager.MediaLibraryManager as mlib

# 指定允许的图片后缀
ALLOWED_IMAGE_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
# 指定允许的音频后缀
ALLOWED_MUSIC_EXTENSIONS = {'mp3'}
# 指定外部资源管理器根目录
mediaLibraryRoot = "../MediaLibrary"

# 初始化外部资源管理器
mediaLibrary = mlib.MediaLibrayManager()

# 标题
caption = "拳皇 In Python"

# 窗口Logo
"""
logo_path 用于指定logo位置，MediaLibaray读取该参数以加载
"""
logo_path = "../MediaLibrary/Pic/KOF_ScreenLogo.jpeg"
screen_logo = mediaLibrary.getScreenLogo()

# 屏幕分辨率
screen_size = (1280, 720)
