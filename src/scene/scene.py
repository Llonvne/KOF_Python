import abc


class Scene(metaclass=abc.ABCMeta):
    """
    场景类，所有场景的抽象类
    """

    def __init__(self, KOF):
        """
        定义所有场景的构造方法， KOF 进程
        """
        self.KOF = KOF

    @abc.abstractmethod
    def event(self, event):
        """
        event 抽象函数，用于 KOF 传入 event 处理
        """
        pass

    def clear(self):
        self.KOF.screen.fill((0, 0, 0))
        self.KOF.bgmService.pause()
