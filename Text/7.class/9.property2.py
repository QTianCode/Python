"""
  作者：LCQT
  日期：2023年05月03日19:42
  项目描述：为属性添加安全保护机制
          在获取或者设置属性值的时候使用setter和getter方法为其添加验证逻辑
          避免对类的某些字段直接访问，比如类的私有变量不应该被外部调用者直击访问或者修改
"""
class TVShow:   # 电视节目类
    list_film = ['战狼2', '红海行动', '西游记女儿国', '熊出没变形记']
    def __init__(self, show):
        self.__show = show
    @property
    def show(self):
        return self.__show    # 返回私有属性
    @show.setter  # .setter用于设置属性值
    def show(self, value):
        if value in TVShow.list_film:  # 判断值是否在列表中
            self.__show = '您选择了 《' + value + '》，稍后将播放'  # 修改返回的值
        else:
            self.__show = '您点播的电影不存在'

tvshow = TVShow('战狼2')   # 创建类的实例
print('正在播放：《', tvshow.show, '》')  # 获取属性值
print('您可以从', TVShow.list_film, '中选择要点播的电影')
tvshow.show = input('请输入您要点播的电影名：')
print(tvshow.show)   # 获取属性值
