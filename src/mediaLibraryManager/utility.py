import os


def get_files(filepath: str) -> dict:
    pathToName = dict()
    for filepath, dirnames, filenames in os.walk(filepath):
        for filename in filenames:
            pathToName[os.path.join(filepath, filename)] = filename
    return pathToName


def getFilenameInsideFolder(folder_path: str) -> list:
    """
    获取文件内部所有文件的名字
    """
    return os.listdir(folder_path)


def getFileSuffix(filename: str) -> str:
    """
    获取文件名的后缀
    """
    return os.path.splitext(filename)[-1][1:]


def getFileName(filename: str) -> str:
    """
    获得文件名不含后缀
    """
    return os.path.splitext(filename)[0]
