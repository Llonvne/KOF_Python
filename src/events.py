import pygame.constants

DIFF = 10000
MUSIC_END = pygame.constants.USEREVENT + 1

"""
开始菜单
ST_xxxx
"""
ST_events = dict()
ST_EVENTS_START = pygame.constants.USEREVENT + DIFF
ST_events["ST_StartGame"] = pygame.constants.USEREVENT + 2

"""
选角色
CH_
"""
CH_EVENTS_START = pygame.constants.USEREVENT + 2 * DIFF
CH_events = dict()


"""
BT_
"""
BT_EVENTS_START = pygame.constants.USEREVENT + 3 * DIFF
BT_events = dict()

"""
结束菜单
ED_xxx
"""
ED_EVENTS_START = pygame.constants.USEREVENT + 4 * DIFF
ED_events = dict()
ED_events["ED_Start"] = ED_EVENTS_START + 1
