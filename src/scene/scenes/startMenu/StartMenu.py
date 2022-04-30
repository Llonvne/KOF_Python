import pygame.draw

from src.scene.scene import Scene


class startMenu(Scene):
    def display(self):
        # 创建一个 50*50 的图像,并优化显示
        face = pygame.Surface((50, 50), flags=pygame.HWSURFACE)
        # 填充颜色
        face.fill(color='pink')
        self.KOF.screen.blit(face, (100, 100))
        pass

    def clear(self):
        pass

    def event(self, event):
        pass
