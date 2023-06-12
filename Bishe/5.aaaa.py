"""
  作者：LCQT
  日期：2023年05月27日15:05
  项目描述：
"""
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


# 设置中文字体为"Microsoft YaHei"
font_path = r'C:\Windows\Fonts\msyh.ttc'
font = FontProperties(fname=font_path)

years = [2010, 2011, 2012, 2013]
population = [650, 720, 810, 891]

plt.plot(years, population, marker='o')
plt.xlabel('时间', fontproperties=font)
plt.ylabel('人数（单位：万人）', fontproperties=font)
plt.title('人口变化', fontproperties=font)

plt.rcParams['interactive'] = False  # 禁用交互模式
plt.show()


