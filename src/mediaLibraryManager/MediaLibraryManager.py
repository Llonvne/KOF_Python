import os

from src.configure import constants
from src.mediaLibraryManager import utility
from src.mediaLibraryManager.Music.MusicHandle import MusicHandle
from src.mediaLibraryManager.Pic.PicHandle import PicHandle
from src.mediaLibraryManager.utility import getFilenameInsideFolder, getFileSuffix, getFileName


class MediaLibrayManager:
    def __init__(self, KOF):
        """
        加载所有图片，以PicHandle类保存在 PicLibrary
        加载所有音乐，以MusicHandle类保存在 MusicLibrary
        初始化BGMService
        """
        # 保存 configure 引用
        self.KOF = KOF

        # 加载所有图片
        self.PicLibrary = dict()
        # 获得所有文件路径 filepath -> filename dict
        pics_path = utility.get_files(os.path.join(constants.mediaLibraryRoot, 'Pic'))
        # 对于每一个路径 和 文件名来说
        for path, name in pics_path.items():
            # 如果他的后缀满足要求
            if utility.getFileSuffix(name) in constants.ALLOWED_IMAGE_EXTENSIONS:
                # 生成 PicHandle 并且添加映射
                self.PicLibrary[getFileName(name)] = PicHandle(path)
        # 加载所有声音
        self.MusicLibrary = dict()
        # 获得所有文件路径 filepaths
        musics_path = utility.get_files(os.path.join(constants.mediaLibraryRoot, 'Music'))
        for path, name in musics_path.items():
            # 如果他的后缀满足要求
            if utility.getFileSuffix(name) in constants.ALLOWED_MUSIC_EXTENSIONS:
                # 生成 PicHandle 并且添加映射
                self.MusicLibrary[getFileName(name)] = MusicHandle(path)
        pass

    def getScreenLogo(self) -> PicHandle:
        """
        返回 screen_logo 以 PicHandle
        """
        return self.PicLibrary[constants.logo_name]

    def getPicFromPath(self, path: str) -> dict[str, PicHandle]:
        """
        返回 path 下所有图片的 PicHandle 集合
        """
        # 初始化字典保存图片
        PicLibrary = {}
        # 获得路径内所有文件名
        pic_name_list = getFilenameInsideFolder(path)
        # 循环每一个文件
        for pic in pic_name_list:
            # 拼接前缀
            pic_path = os.path.join(path, pic)
            # 如果是文件夹，且后缀满足规范
            if os.path.isfile(pic_path) and getFileSuffix(pic_path) in constants.ALLOWED_IMAGE_EXTENSIONS:
                # 创建 PicHandle 对象 并建立文件名到 PicHandle 的映射
                PicLibrary[getFileName(pic)] = PicHandle(pic_path)
        # 返回 PicHandle 集合
        return PicLibrary

    def getMusicHandle(self, music):
        return self.MusicLibrary[music]
