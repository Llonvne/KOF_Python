import abc
import pygame


class GameEvent(metaclass=abc.ABCMeta):
    def __init__(self):
        self.custom_event = set()
        pass

    def isCustom(self, event: pygame.event.Event) -> bool:
        if event is None:
            return False
        return event.type in self.custom_event

    def getEvent(self, uniqueID: int, message: dict) -> pygame.event.Event:
        self.custom_event.add(uniqueID)
        return pygame.event.Event(uniqueID, message)

    @staticmethod
    def postEvent(event: pygame.event.Event) -> bool:
        return pygame.event.post(event)
