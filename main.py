"""使用GitHub Actions每日自动触发东大信息化中的东豆奖励。
其中的身份验证借助SEU-Auth项目（https://github.com/Golevka2001/SEU-Auth）中的seu_auth_mobile.py脚本完成。

免责声明：
1. 本项目仅用于学习交流，不得用于任何违反法律法规、侵犯他人权益的行为；
2. 由于使用本项目造成的任何后果，均由使用者自行承担；
3. 本项目不提供任何形式的保证，亦不承担任何责任。

函数说明：
query_seu_points()函数用于查询用户在东大信息化中的东豆余额；
earn_seu_points()函数用于触发特定类型的东豆奖励；
主函数中，使用多线程触发不同类型的东豆奖励，直至达到奖励上限。

使用方法：
详见README.md

Author: Golevka2001 (https://github.com/Golevka2001)
Email: gol3vka@163.com
Date: 2023/11/05
License: GPL-3.0 License
"""

import os
import threading
from time import sleep

import requests

from seu_auth_mobile import seu_login


def query_seu_points(username: str,
                     password: str,
                     session: requests.Session = None):
    """查询东大信息化中的东豆余额。

    Args:
        username: 一卡通号
        password: 统一身份认证密码
        session: 登录移动端身份认证平台后的session

    Returns:
        session: 用于继续会话
        user_points: 查询到的东豆余额
    """
    try:
        # 若未传入session，则需要登录移动端身份认证平台
        if not session:
            session = seu_login(username, password)
            if not session:
                raise Exception('移动端身份认证平台登录失败')
        # 查询东豆余额
        url = (
            'http://apoint.seu.edu.cn/_web/_customizes/seu/point/api/findUserPoint.rst?'
            '_p=YXM9MiZwPTEmbT1OJg__'
            '&act=1'
            f'&loginName={username}')

        res = session.get(url)
        if res.status_code != 200:
            raise Exception(f'[{res.status_code}, {res.reason}]')

        user_points = res.json()['result']['data']['score']
        return session, user_points
    except Exception as e:
        print('东豆余额查询失败，错误信息：', e)
        return None, None


def earn_seu_points(username: str,
                    password: str,
                    type_id: int = 1,
                    session: requests.Session = None):
    """触发东大信息化中的东豆奖励。
    注：东豆奖励有每日/每周上限，且由后端判断，无法超出。

    Args:
        username: 一卡通号
        password: 统一身份认证密码
        type_id: 触发奖励类型（详见README.md）
        session: 登录移动端身份认证平台后的session

    Returns:
        session: 用于继续会话
        limit_reached: 是否达到奖励上限
    """
    try:
        # 若未传入session，则需要登录移动端身份认证平台
        if not session:
            session = seu_login(username, password)
            if not session:
                raise Exception('移动端身份认证平台登录失败')
        # 触发东豆奖励
        # Headers仍为非必须
        headers = {
            'Accept-Encoding':
            'gzip,deflate',
            'Connection':
            'Keep-Alive',
            'Content-Type':
            'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie2':
            '$Version=1',
            'Host':
            'apoint.seu.edu.cn',
            'User-Agent':
            'Mozilla/5.0 (Linux; Android 13; Pixel 5 Build/TQ3A.230605.012; wv) '
            'AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.131 Safari/537.36 iPortal/41',
        }
        session.headers.update(headers)
        url = 'http://apoint.seu.edu.cn/_web/_customizes/seu/point/api/addPoint.rst?'
        data = {
            '_p': 'YXM9MiZwPTEmbT1OJg__',
            'act': '1',
            'loginName': username,
            'typeId': type_id,
        }
        # 当typeId为3时（查看应用），需要携带appId参数
        if data['typeId'] == 3:
            data['appId'] = '1'

        res = session.post(url, data=data)
        if res.status_code != 200:
            raise Exception(f'[{res.status_code}, {res.reason}]')

        print('触发东豆奖励成功，返回信息：', res.json())
        return session, (res.json()['errorMsg'] != '')
    except Exception as e:
        print('触发东豆奖励失败，错误信息：', e)
        return None, False


if __name__ == "__main__":
    # 使用 GitHub Actions 时，需要在 Secrets 中设置 USERNAME 和 PASSWORD
    username = os.environ['USERNAME']
    password = os.environ['PASSWORD']

    # 东豆奖励类型
    # 1-登录
    # 2-查看文章
    # 3-查看应用
    # 5-开启客户端
    bonus_type_list = [1, 2, 3, 5]

    # 登录移动端身份认证平台
    login_flag = False
    while not login_flag:
        session = seu_login(username, password)
        if session:
            login_flag = True
        else:
            print('登录失败，正在重试...')
            sleep(3)

    # 查询东豆余额
    session, init_points = query_seu_points(username, password, session)

    # 定义多线程函数
    def thread_func(username, password, session, bonus_type):
        limit_reached = False
        while not limit_reached:
            session, limit_reached = earn_seu_points(username, password,
                                                     bonus_type, session)
        print(f'奖励类型{bonus_type}已达上限')

    # 多线程触发东豆奖励
    threads = []
    for bonus_type in bonus_type_list:
        t = threading.Thread(target=thread_func,
                             args=(username, password, session, bonus_type))
        threads.append(t)
        t.start()

    # 等待所有线程完成
    for t in threads:
        t.join()

    # 查询东豆余额
    session, final_points = query_seu_points(username, password, session)
    print(f'东豆余额：{init_points} -> {final_points}')
