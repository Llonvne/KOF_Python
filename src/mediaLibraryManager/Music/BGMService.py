import pygame

from src import events
from src.mediaLibraryManager import MediaLibraryManager


class BGMService:
    """
    BGMService
    提供BGM 启停服务，控制BGM的播放
    BGM以 MusicHandle 列表传入，请使用 MusicHandle 内部的接口 实现播放和停止
    """

    def __init__(self, mediaLibraryManager: MediaLibraryManager):
        """
        传入 MusicHandle 列表，初始化BGM队列
        """
        pygame.mixer.init()
        pygame.mixer.music.load("E:\KOF_Python\MediaLibrary\Music\BGM1.mp3")
        pygame.mixer.music.set_endevent(events.MUSIC_END)

    def play(self):
        """
        循环播放，列表内音乐
        """
        pygame.mixer.music.play(1)
        pass

    def pause(self):
        """
        暂停播放，播放头不变
        """
        pygame.mixer.music.pause()
        pass

    def unpause(self):
        """
        取消暂停播放，播放头不变
        """
        pygame.mixer.music.unpause()
        pass
