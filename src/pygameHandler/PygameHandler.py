# 导入 pygame 和 config
import pygame
from src import config


class PygameHandler:
    def __init__(self):
        # 初始化 pygame
        pygame.init()
        # 设置标题
        pygame.display.set_caption(config.caption)
        # 设置 screen_logo
        pygame.display.set_icon(config.screen_logo.pygamePic())
        # 设置 screen 属性
        self.screen = pygame.display.set_mode(config.screen_size)
        # 播放BGM
        music = config.mediaLibrary.getMusicHandle("BGM1")
        music.play()

    def run(self):
        # 运行结束标记符号
        running = True
        while running:
            # 获取事件
            for event in pygame.event.get():
                # 如果按下了退出按钮
                if event.type == pygame.QUIT:
                    running = False
