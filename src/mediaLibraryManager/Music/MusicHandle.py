import pygame


class MusicHandle:
    """
    MusicHandle
    初始化： 使用音乐文件路径初始化
    提供以下三个接口，控制音乐播放
    每一个对象仅为一首音乐服务，更换音乐需要新建对象

    music_path: 音乐文件路径 str 代表文件路径
    """

    def __init__(self, music_path):
        if pygame.mixer.get_init() is None:
            pygame.mixer.init()
        """以音乐文件路径初始化对象，初始化播放头为开始"""
        self.music_path = music_path
        self.controller = pygame.mixer.Sound(music_path)
        pass

    def play(self):
        """播放音乐，从播放头开始播放"""
        self.controller.play()
        pass

    def stop(self):
        """停止播放，播放头为开始"""
        self.controller.fadeout(100)
