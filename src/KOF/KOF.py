# 导入 pygame 和 config
import pygame

from src.characters.Characters import Characters
from src.configure import constants
from src.gameEvent.GameEvent import GameEvent
from src.mediaLibraryManager.MediaLibraryManager import MediaLibrayManager
from src.mediaLibraryManager.Music.BGMService import BGMService
from src.scene.scene import Scene
from src.scene.scenes.ChooseChar.ChooseChar import ChooseChar
from src.scene.scenes.battle.Battle import Battle
from src.scene.scenes.endMenu.EndMenu import EndMenu
from src.scene.scenes.startMenu.StartMenu import startMenu


class KOF:
    def __init__(self):
        # 初始化 pygame
        pygame.init()
        # 初始化外部资源管理器
        self.mediaLibrary = MediaLibrayManager(self)
        # 设置标题
        pygame.display.set_caption(constants.caption)
        # 设置 screen_logo
        pygame.display.set_icon(self.mediaLibrary.getScreenLogo().pygamePic())
        # 设置 screen 属性
        self.screen = pygame.display.set_mode(constants.screen_size)
        # 初始化BGM服务
        self.bgmService = BGMService(self.mediaLibrary)
        # self.bgmService.play("BGM1")
        # 建立事件管理器
        self.eventsManager = GameEvent()

    def run(self):

        startM = startMenu(self)
        choose = ChooseChar(self)
        battleM = Battle(self)
        endM = EndMenu(self)

        nowScene: Scene = startM

        # 在队列中添加 开始菜单界面
        self.eventsManager.postEvent(self.eventsManager.getEvent(constants.ST_STRAT, {}))

        s1 = Characters(self, "Ashkofxii", (50, 50))
        self.screen.blit(s1.pic, s1.rect)

        # 运行结束标记符号
        running = True
        while running:
            # 事件过滤
            # pygame.event.set_allowed(None)
            for event in pygame.event.get():
                # 如果按下了退出按钮
                if event.type == pygame.QUIT:
                    running = False
                # if event.type == constants.ST_STRAT:
                #     nowScene = startM
                # if event.type == constants.ST_NEXT:
                #     nowScene = choose
                #     choose = ChooseChar(self)
                # nowScene.event(event)
            pygame.display.update()
