import pygame


class Characters(pygame.sprite.Sprite):
    def __init__(self, KOF, charName, location):
        pygame.sprite.Sprite.__init__(self)
        self.pic = KOF.mediaLibrary.PicLibrary[charName].pygamePic()
        self.rect = self.pic.get_rect()
        self.rect.topleft = location
