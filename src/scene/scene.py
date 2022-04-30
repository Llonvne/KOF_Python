import abc


class Scene(metaclass=abc.ABCMeta):
    """
    场景类，所有场景的抽象类
    """

    @abc.abstractmethod
    def event(self, event):
        """
        event 抽象函数，用于 GameMainProcess 传入 event 处理
        """
        pass
