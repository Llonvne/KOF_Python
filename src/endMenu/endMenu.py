import pygame.event

from src import events
from src.scene.scene import Scene


class endMenu(Scene):
    def __init__(self, screen, config):
        self.screen = screen
        self.config = config
        pass

    def BGMandBG(self):
        self.config.mediaLibrary.MusicLibrary[self.config.winnerSong].play()
        pass

    def winnerGIF(self):
        pass

    def displayKO(self):
        pass

    def button(self):
        pass

    def event(self, event):
        if event == events.ED_PLAY:
            self.BGMandBG()
        pass
