# 导入 pygame 和 config
import pygame

from src.config import Config
from src import events
from src.scene.scenes.endMenu.EndMenu import EndMenu


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
        # 初始化事件管理器
        self.eventsManager = events.GameEvent()

    def run(self):

        startM = None
        choose = None
        battleM = None
        endM = None

        # 运行结束标记符号
        running = True
        while running:
            # 事件过滤
            # pygame.event.set_allowed(None)
            for event in pygame.event.get():
                print(event)
                # 如果按下了退出按钮
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == events.MUSIC_END:
                    self.config.bgmService.play()
                # elif self.eventsManager.isInST(event.type):
                #     if startM is None:
                #         startM = startMenu(self.screen, self.config)
                #     startM.event(event.type)
                # elif self.eventsManager.isInCH(event.type):
                #     if choose is None:
                #         choose = chooseChar()
                #     choose.event(event.type)
                # elif self.eventsManager.isInBT(event.type):
                #     if battleM is None:
                #         battleM = battle()
                #     battleM.event(event.type)
                elif event.type == events.ED_PLAY:
                    if endM is None:
                        endM = EndMenu(self.screen, self.config)
                    endM.event(event.type)

            pygame.display.flip()  # 更新屏幕内容
