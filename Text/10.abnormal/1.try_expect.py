"""
  作者：LCQT
  日期：2023年05月04日21:17
  项目描述：模拟异常时用 try...except 捕获异常
"""
def division():
    '''功能：分苹果'''
    print('\n===============分苹果了===============\n')
    apple = int(input('请输入苹果的个数：'))
    children = int(input('请输入来了几个小朋友：'))
    result = apple//children
    remain = apple-result*children
    if remain>0:
        print(apple, '个苹果，平均分给',children, '个小朋友，每人分', result, '个，剩下', remain, '个。')
    else:
        print(apple, '个苹果，平均分给', children, '个小朋友，每人分', result, '个。')
if __name__ == '__main__':
    try:
        division()
    except ZeroDivisionError:  # 除数为0的异常
        print('\n出错了，——苹果不能被0个小朋友分！')
    except ValueError as ve:
        print('输入错误，请输入整数个', ve)
    # except (ZeroDivisionError, ValueError) as e:  # 也可以在一句里面抛出异常
       # print('输入错误', e)
