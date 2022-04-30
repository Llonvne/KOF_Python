import abc
import pygame

class GameEvent(metaclass=abc.ABCMeta):
    def __init__(self):
        pass

    @staticmethod
    def getEvent(uniqueID: int, message: dict) -> pygame.event.Event:
        return pygame.event.Event(uniqueID, message)

    @staticmethod
    def postEvent(event: pygame.event.Event) -> bool:
        return pygame.event.post(event)
