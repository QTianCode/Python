"""
  作者：LCQT
  日期：2023年05月04日18:25
  项目描述：高度和宽度
"""
_width = 800  # 保护类型的全局变量（宽度）
_height = 600  # 保护类型的全局变量（高度）
def change(w,h):
    global _width  # 全局变量
    global _height  # 全局变量
    _width = w  # 重新为宽度赋值
    _height = h  # 重新为高度赋值
def getWidth():
    global _width  # 全局变量
    return _width
def getHeight():
    global _height  # 全局变量
    return _height
