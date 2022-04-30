import pygame

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
        self.mediaLibraryManager = mediaLibraryManager
        # pygame.mixer.music.set_endevent(events.MUSIC_END)

    def play(self, musicName):
        """
        循环播放，列表内音乐
        """
        pygame.mixer.music.load(self.mediaLibraryManager.MusicLibrary[musicName].music_path)
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
