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
        pygame.display.flip()  # 更新屏幕内容
        pass

    def clear(self):
        self.KOF.screen.fill((0,0,0))
        pass

    def event(self, event):
        # 用于获取鼠标的坐标，触发范围为（100，50）-（400，247）
        ball_x, ball_y = pygame.mouse.get_pos()
        mousepos=pygame.mouse.get_pressed()
        if 100 <= ball_x <= 400 and 50 <= ball_y <= 247 and mousepos[0]==1:
            self.clear()
            self.next()
        if event.type == constants.ST_STRAT:
            self.display()
        pass

    def next(self):
        self.KOF.eventsManager.postEvent(
            self.KOF.eventsManager.getEvent(constants.ST_NEXT, {})
        )
