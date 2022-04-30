import pygame.draw

from src.configure import constants
from src.scene.scene import Scene


class startMenu(Scene):
    def display(self):
        # 调用资源管理器中的背景图片
        Background = self.KOF.mediaLibrary.PicLibrary['KOF_StarBG1'].pygamePic()
        Gobutton = self.KOF.mediaLibrary.PicLibrary['GO2'].pygamePic()
        Gif1 = self.KOF.mediaLibrary.PicLibrary['Ashkofxii'].pygamePic()
        self.KOF.bgmService.play("BGM1")
        # 打印在屏幕上
        self.KOF.screen.blit(Background, (0, 0))
        self.KOF.screen.blit(Gobutton, (100, 50))
        self.KOF.screen.blit(Gif1, (300, 100))
        pass

    def clear(self):
        pass

    def event(self, event):
        if event.type == constants.ST_STRAT:
            self.display()
        pass

    def next(self):
        self.KOF.eventsManager.postEvent(
            self.KOF.eventsManager.getEvent(constants.ST_NEXT, {})
        )
