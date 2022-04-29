"""
config: KOF 关键参数配置目录
"""
import os

# 导入外部资源管理器
import mediaLibraryManager.MediaLibraryManager as mlib
from src.mediaLibraryManager.Music.BGMService import BGMService


class Config:
    def __init__(self):
        # 指定允许的图片后缀
        self.ALLOWED_IMAGE_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
        # 指定允许的音频后缀
        self.ALLOWED_MUSIC_EXTENSIONS = {'mp3'}
        # 指定外部资源管理器根目录
        self.mediaLibraryRoot = os.path.join(os.pardir, "MediaLibrary")
        # 初始化外部资源管理器
        self.mediaLibrary = mlib.MediaLibrayManager(self)
        # 初始化BGM服务
        self.bgmService = BGMService(self.mediaLibrary)

        # 标题
        self.caption = "拳皇 KOF"

        # 窗口Logo
        """
        logo_path 用于指定logo位置，MediaLibaray读取该参数以加载
        """
        self.logo_name = "KOF_ScreenLogo"
        self.screen_logo = self.mediaLibrary.getScreenLogo()

        # 屏幕分辨率
        self.screen_size = (1280, 720)

