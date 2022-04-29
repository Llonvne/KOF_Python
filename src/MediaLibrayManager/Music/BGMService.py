class BGMService():
    """
    BGMService
    提供BGM 启停服务，控制BGM的播放
    BGM以 MusicHandle 列表传入，请使用 MusicHandle 内部的接口 实现播放和停止
    """
    def __init__(self,BGMs):
        """
        传入 MusicHandle 列表，初始化BGM队列
        """
        pass

    def play(self):
        """
        循环播放，列表内音乐
        """
        pass

    def pause(self):
        """
        暂停播放，播放头不变
        """
        pass