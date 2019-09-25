# 计算嵌套在一个特定目录中的所有文件和目录的总磁盘使用情况
# os.path.getsize(path) 即时磁盘空间大小
# os.path.isdir(path)   目录则返回True， 否则返回False
# os.path.listdir(path) 返回所有子目录中的名称
# os.path.join(path, filename) 返回文件完整路径

import os

def disk_usage(path):
    """ Return the number of bytes used by file/folder and any descendents """
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            total += disk_usage(os.path.join(path, filename))
    print('{0:<7}'.format(total), path)
    return total

if __name__ == '__main__':
    print('disk_usage for test')
    disk_usage('./')

