import os

# 指定允许的图片后缀
ALLOWED_IMAGE_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
# 指定允许的音频后缀
ALLOWED_MUSIC_EXTENSIONS = {'mp3'}
# 指定外部资源管理器根目录
mediaLibraryRoot = os.path.join(os.pardir,os.pardir,"MediaLibrary")

# 标题
caption = "拳皇 KOF"

# 窗口Logo
logo_name = "KOF_ScreenLogo"

# 屏幕分辨率
screen_size = (1280, 720)

# Winner Song
winnerSong = "BGM31"
