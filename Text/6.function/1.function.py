"""
  作者：LCQT
  日期：2023年05月01日19:43
  项目描述：函数的创建与调用
"""
def filterchar(string):
    '''
    功能：过滤危险字符（如傻逼），并且将过滤后的结果输出
    :param string:要过滤的字符串
    :return:无返回值
    '''
    import re
    pattern = r'(傻逼)|(日)|(他妈的)|(666)|(大爷)'  # 模式字符串
    match = re.sub(pattern, "*", string)
    print(match)
#def empty():
    #pass
about = '6666啊，傻逼，我日你大爷。'
filterchar(about)
about1 = '我是一个大帅哥。'
filterchar(about1)
