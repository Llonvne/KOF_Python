import pygame.draw

from src.scene.scene import Scene


class startMenu(Scene):
    def display(self):
        #调用资源管理器中的背景图片
        Background=self.KOF.mediaLibrary.PicLibrary['KOF_StarBG2'].pygamePic()
        Gobutton= self.mediaLibrary.PicLibrary['GO1'].pygamePic()
        self.config.bgmService.play("BGM1")
        #打印在屏幕上
        self.screen.blit(Background, (0, 0))
        self.screen.blit(Gobutton, (30,30))
        pass

    def clear(self):
        pass

    def event(self, event):
        pass
