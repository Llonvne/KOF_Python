# 导入 pygame 和 config
import pygame

from src.configure import constants
from src.gameEvent.GameEvent import GameEvent
from src.mediaLibraryManager.MediaLibraryManager import MediaLibrayManager
from src.mediaLibraryManager.Music.BGMService import BGMService
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

        startM = None
        choose = None
        battleM = None
        endM = None

        # 在队列中添加 开始菜单界面
        self.eventsManager.postEvent(self.eventsManager.getEvent(constants.ST_STRAT, {}))

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
                if event.type == constants.ST_STRAT:
                    if startM is None:
                        startM = startMenu(self)
                    startM.event(event.type)

            pygame.display.flip()  # 更新屏幕内容
