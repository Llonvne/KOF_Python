# 导入 pygame 和 config
import pygame

from src.config import Config
from src import events
from src.mediaLibraryManager.Music.BGMService import BGMService


class KOF:
    def __init__(self):
        # 初始化 pygame
        pygame.init()
        # 初始化 config
        self.config = Config()
        # 设置标题
        pygame.display.set_caption(self.config.caption)
        # 设置 screen_logo
        pygame.display.set_icon(self.config.screen_logo.pygamePic())
        # 设置 screen 属性
        self.screen = pygame.display.set_mode(self.config.screen_size)
        # 播放BGM
        self.config.bgmService.play()

    def run(self):
        # 运行结束标记符号
        running = True
        while running:
            # 获取事件
            for event in pygame.event.get():
                # 如果按下了退出按钮
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == events.MUSIC_END:
                    self.config.bgmService.play()