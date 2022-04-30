from src.scene.scene import Scene


class EndMenu(Scene):
    """
    endMenu 类 实现结束界面的控制
    """

    def BGMandBG(self):
        self.KOF.mediaLibrary.MusicLibrary['BGM1'].play()
        pass

    def winnerGIF(self):
        pass

    def displayKO(self):
        pass

    def button(self):
        pass

    def event(self, event):
        if event.type == events.ED_PLAY:
            self.BGMandBG()
        pass
