# 导入 pygame 以返回pygame支持的格式
import pygame


class PicHandle:
    """
    图形对象，使用图像路径初始化
    """

    def __init__(self, pic_path):
        """
        以图像路径初始化对象
        """

        # 懒加载
        self._pic_for_pygame = None

        # 图像路径
        self.pic_path = pic_path

    def pygamePic(self):
        """
        返回Pygame支持的图片格式 screen
        """

        # 采用懒加载，除非调用，否则不加载
        if self._pic_for_pygame is None:
            self._pic_for_pygame = pygame.image.load(self.pic_path)
        return self._pic_for_pygame
