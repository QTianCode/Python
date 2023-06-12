"""
  作者：LCQT
  日期：2023年06月07日14:58
  项目描述：绘制彩色螺旋图
"""
# 彩色螺旋图
import turtle  # turtle是python自带的绘图库
import random  # random是python自带的生成随机数的库


# speed：为绘图速度，0是最快的
# background_color: 为画板颜色，默认给的黑色
def color_spiral(spiral_num, speed=0, background_color="black"):
    turtle.speed(speed)
    turtle.bgcolor(background_color)
    turtle.setpos(-20, 20)  # 初始位置
    turtle.colormode(255)  # 颜色取值为0-55
    for i in range(spiral_num):
        r = random.randint(0, 255)  # 随机生成0-255的整数值
        g = random.randint(0, 255)  # 随机生成0-255的整数值
        b = random.randint(0, 255)  # 随机生成0-255的整数值
        turtle.pencolor(r, g, b)  # 画笔颜色
        turtle.forward(40 + i)  # 划线长度
        turtle.right(91)  # 顺时针旋转91度

    turtle.mainloop()  # 结束时，页面停留


# 函数调用，传递100次画笔调用，速度为0.2,背景为白色
color_spiral(300, 0.2, "white")
