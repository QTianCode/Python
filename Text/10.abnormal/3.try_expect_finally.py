"""
  作者：LCQT
  日期：2023年05月05日09:46
  项目描述：try_expect_finally语句
"""
def division():
    '''功能：分苹果'''
    print('\n===============分苹果了===============\n')
    apple = int(input('请输入苹果的个数：'))
    children = int(input('请输入来了几个小朋友：'))
    result = apple//children
    remain = apple-result*children
    if remain > 0:
        print(apple, '个苹果，平均分给',children, '个小朋友，每人分', result, '个，剩下', remain, '个。')
    else:
        print(apple, '个苹果，平均分给', children, '个小朋友，每人分', result, '个。')
if __name__ == '__main__':
    try:
        division()
    except (ZeroDivisionError, ValueError) as e:  # 也可以在一句里面抛出异常
        print('输入错误', e)
    finally:
        print('完成分苹果一次...')