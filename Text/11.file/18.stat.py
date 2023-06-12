"""
  作者：LCQT
  日期：2023年05月05日20:24
  项目描述：获取文件的基本信息
"""
import os
def formatTime(Longtime):
    '''格式化时间'''
    import time
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(Longtime))
def formatByte(number):
    '''格式化文件大小'''
    for (scale, label) in [(1024*1024*1024,'GB'), (1024*1024,'MB'), (1024,'KB')]:
        if number >= scale:  # 大于等于1KB
            return '%.3f %s' % (number*1.0/scale, label)
        elif number == 1:
            return '1 字节'
        else:  # 小于1KB
            byte = '%.3f' % (number or 0)
    return (byte[:-3] if byte.endswith('.00') else byte) + '字节'


fileinfo = os.stat('for_our.jpg')  # 获取文件的基本信息
number = formatByte(fileinfo.st_size)  # 给函数传递文件大小
# 获取文件的完整路径
print('文件完整路径：', os.path.abspath('for_our.jpg'))
print('索引号：', fileinfo.st_ino)
print('设备名：', fileinfo.st_dev)
print('文件大小：', number)
print('最后一次访问时间：', formatTime(fileinfo.st_atime))
print('最后一次修改时间：', formatTime(fileinfo.st_mtime))
print('最后一次状态变化的时间：', formatTime(fileinfo.st_ctime))