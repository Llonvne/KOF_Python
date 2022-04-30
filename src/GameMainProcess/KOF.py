# 导入 pygame 和 config
import pygame

from src.ChooseChar.chooseChar import chooseChar
from src.battle.battle import battle
from src.config import Config
from src import events, gameStatus
from src.endMenu.endMenu import endMenu
from src.startMenu.startMenu import startMenu


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

    def run(self):
        status = gameStatus.START_MENU

        startM = None
        choose = None
        battleM = None
        endM = None

        # 运行结束标记符号
        running = True
        while running:

            # 事件过滤
            pygame.event.set_allowed(None)

            for event in pygame.event.get():
                # 如果按下了退出按钮
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == events.MUSIC_END:
                    self.config.bgmService.play()
                elif event.type in events.ST_events.values():
                    if startM is None:
                        startM = startMenu(self.screen, self.config)
                    startM.event(event.type)
                elif event.type in events.CH_events.values():
                    if choose is None:
                        choose = chooseChar()
                    choose.event(event)
                elif event.type in events.BT_events.values():
                    if battleM is None:
                        battleM = battle()
                    battleM.event(event)
                elif event.type in events.ED_events.values():
                    if endM is None:
                        endM = endMenu()
                    endM.event(event)

            pygame.display.flip()  # 更新屏幕内容
