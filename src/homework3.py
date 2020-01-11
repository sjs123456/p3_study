# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : sjs

# 装饰器

webPage = ['home', 'finance', 'book']
weChatAccountData = 'weChatAccountData.txt'
jdAccountData = 'jdAccountData.txt'

def login_v(authType, fileName):
    """
    接收用户的账号密码并进行验证，验证成功返回True
    :param authType: 需要进行登录的账号的类型
    :param fileName: 需要进行登录的账号存储的文件名
    :return:
    """
    # 打开文件获取所有的用户账户和密码信息
    with open(fileName, 'r') as f:
        data = eval(f.read())
    accountIdList = []
    # 将账号存入列表
    for i in data:
        accountIdList.append(i['accountId'])
    # 接收用户输入
    accountId = input( '请输入您的%s账号\n>>> : '  % authType)
    password = input( '请输入您的%s密码\n>>> : ' % authType)
    # 判断密码和账号是否存在且正确
    if accountId in filter(lambda x : x == accountId, accountIdList)  and \
            password == data[accountIdList.index(accountId)]['password']:
        return True
    else:
        print('账号密码有误，请重试！')
        # 错误后重新进行登录验证
        login_v(authType, fileName)

# 添加一个是否登录的字段
isLogin = False

def login(authType = 'JD'):
    """
    获取登录账号的类型并进行登录的装饰器函数
    :param authType:
    :return:
    """
    def outer(func):
        def inner(*args, **kwargs):
            global isLogin
            # 如果未登录
            if not isLogin:
                # 如果要登录JD类型的账号且进行登录验证
                if authType == 'JD' and login_v(authType, jdAccountData):
                        func(*args, **kwargs)
                # 如果要登录weChat类型的账号且进行登录验证
                if authType == 'weChat' and login_v(authType, weChatAccountData):
                        func(*args, **kwargs)
                # 登录成功后改变登录状态
                isLogin = True
            # 如果已登录，直接执行目标函数
            else:
                func(*args, **kwargs)
        return inner
    return outer


@login(authType='JD')
def home():
    print('welcome to home page ....')

@login(authType='weChat')
def finance():
    print( 'welcome to finance page ....' )

@login(authType='JD')
def book():
    print( 'welcome to book page ....' )


def runApp():
    while True:
        for index, pageName in enumerate( webPage ):
            print( index, '.', '\t', pageName )
        revPage = input( '请输入要进入的页面\n>>> : ' )
        if revPage == '0' or revPage.upper() == 'HOME':
            home()
        elif revPage == '1' or revPage.upper() == 'FINANCE':
            finance()
        elif revPage == '2' or revPage.upper() == 'BOOK':
            book()
        elif revPage == 'quit':
            break
        else:
            print('您的输入有误，请重新输入')

if __name__ == "__main__":
    runApp()