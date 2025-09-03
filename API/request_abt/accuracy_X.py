from flask import Flask, jsonify, request
import mysql.connector
from datetime import datetime
import subprocess
import json
from request_abt import get_request
import config.config
from data_process import http_yanzheng
import IP_address

"""
################################################################################
# 验证一次的代理获取模块                                                         #
#                                                                              #
################################################################################
"""
def accuracy_1():
    try:
        print()
        # 设置验证次数
        yanzhengcishu = 1
        proxies = None
        # 读取文件
        file_path = 'output/http.txt'
        # 验证信息
        with open(file_path,'r') as file:
            line_count = sum (1 for _ in file)
        print('---------------------------------------------------------')
        print(f'验证后的信息共计 {line_count} 行。已经保存到了:{file_path} ')
        print('---------------------------------------------------------')
        # 读取并且返回
        proxies = accuracy_1_http()
        if proxies is None:

            proxies = []
            return yanzhengcishu,proxies
        return yanzhengcishu,proxies,line_count
    except Exception as e :
        print('小问题,不要慌')
        proxies = []
        return yanzhengcishu,proxies,line_count
    return

# 获取数据并输出1
def accuracy_1_http():
    """读取 output/http.txt 文件并返回内容作为列表"""
    try:
        with open('output/http.txt', 'r') as file:
            # 读取所有行并去掉空行
            lines = file.readlines()
            # 移除每行末尾的换行符，并返回一个列表
            return [line.strip() for line in lines if line.strip()]
    except FileNotFoundError:
        return None
"""
################################################################################
# 验证两次的代理获取模块                                                         #
#                                                                              #
################################################################################
"""
def accuracy_2():
    try:
        print()
        # 设置验证次数
        yanzhengcishu = 2
        proxies = None
        # 读取文件
        file_path = 'output/http2.txt'
        # 验证信息
        with open(file_path,'r') as file:
            line_count = sum (1 for _ in file)
        print('---------------------------------------------------------')
        print(f'验证后的信息共计 {line_count} 行。已经保存到了:{file_path} ')
        print('---------------------------------------------------------')
        # 读取并且返回
        proxies = accuracy_2_http()
        if proxies is None:

            proxies = []
            return yanzhengcishu,proxies
        return yanzhengcishu,proxies,line_count
    except Exception as e :
        print('小问题,不要慌')
        proxies = []
        return yanzhengcishu,proxies,line_count
    return

# 获取数据并输出2
def accuracy_2_http():
    """读取 output/http2.txt 文件并返回内容作为列表"""
    try:
        with open('output/http2.txt', 'r') as file:
            # 读取所有行并去掉空行
            lines = file.readlines()
            # 移除每行末尾的换行符，并返回一个列表
            return [line.strip() for line in lines if line.strip()]
    except FileNotFoundError:
        return None
    
"""
################################################################################
# 验证三次的代理获取模块                                                         #
#                                                                              #
################################################################################
"""
def accuracy_3():
    try:
        print()
        # 设置验证次数
        yanzhengcishu = 3
        proxies = None
        # 读取文件
        file_path = 'output/http3.txt'
        # 验证信息
        with open(file_path,'r') as file:
            line_count = sum (1 for _ in file)
        print('---------------------------------------------------------')
        print(f'验证后的信息共计 {line_count} 行。已经保存到了:{file_path} ')
        print('---------------------------------------------------------')
        # 读取并且返回
        proxies = accuracy_3_http()
        if proxies is None:

            proxies = []
            return yanzhengcishu,proxies
        return yanzhengcishu,proxies,line_count
    except Exception as e :
        print('小问题,不要慌')
        proxies = []
        return yanzhengcishu,proxies,line_count
    return

# 获取数据并输出3
def accuracy_3_http():
    """读取 output/http2.txt 文件并返回内容作为列表"""
    try:
        with open('output/http3.txt', 'r') as file:
            # 读取所有行并去掉空行
            lines = file.readlines()
            # 移除每行末尾的换行符，并返回一个列表
            return [line.strip() for line in lines if line.strip()]
    except FileNotFoundError:
        return None
    
"""
################################################################################
# 没有验证的代理获取模块                                                         #
#                                                                              #
################################################################################
"""
def accuracy_4():
    try:
        print()
        # 设置验证次数
        yanzhengcishu = 0
        proxies = None
        # 读取文件
        file_path = 'output/proxy.txt'
        # 验证信息
        with open(file_path,'r') as file:
            line_count = sum (1 for _ in file)
        print('---------------------------------------------------------')
        print(f'信息共计 {line_count} 行。已经保存到了:{file_path} ')
        print('---------------------------------------------------------')
        # 读取并且返回
        proxies = accuracy_4_http()
        if proxies is None:

            proxies = []
            return yanzhengcishu,proxies
        return yanzhengcishu,proxies,line_count
    except Exception as e :
        print('小问题,不要慌')
        proxies = []
        return yanzhengcishu,proxies,line_count
    return

# 获取数据并输出4
def accuracy_4_http():
    """读取 output/proxy.txt 文件并返回内容作为列表"""
    try:
        with open('output/proxy.txt', 'r') as file:
            # 读取所有行并去掉空行
            lines = file.readlines()
            # 移除每行末尾的换行符，并返回一个列表
            return [line.strip() for line in lines if line.strip()]
    except FileNotFoundError:
        return None
    

"""
################################################################################
# 验证一次socks5的代理获取模块                                                   #
#                                                                              #
################################################################################
"""
def accuracy_1_socks5():
    try:
        print()
        # 设置验证次数
        yanzhengcishu = 1
        proxies = None
        # 读取文件
        file_path = 'output/socks5_w.txt'
        # 验证信息
        with open(file_path,'r') as file:
            line_count = sum (1 for _ in file)
        print('---------------------------------------------------------')
        print(f'验证后的信息共计 {line_count} 行。已经保存到了:{file_path} ')
        print('---------------------------------------------------------')
        # 读取并且返回
        proxies = accuracy_1_socks5_run()
        if proxies is None:

            proxies = []
            return yanzhengcishu,proxies
        return yanzhengcishu,proxies,line_count
    except Exception as e :
        print('小问题,不要慌')
        proxies = []
        return yanzhengcishu,proxies,line_count
    return

# 获取数据并输出1
def accuracy_1_socks5_run():
    """读取 output/socks5_w.txt 文件并返回内容作为列表"""
    try:
        with open('output/socks5_w.txt', 'r') as file:
            # 读取所有行并去掉空行
            lines = file.readlines()
            # 移除每行末尾的换行符，并返回一个列表
            return [line.strip() for line in lines if line.strip()]
    except FileNotFoundError:
        return None

"""
################################################################################
# 验证二次socks5的代理获取模块                                                   #
#                                                                              #
################################################################################
"""
def accuracy_2_socks5():
    try:
        print()
        # 设置验证次数
        yanzhengcishu = 2
        proxies = None
        # 读取文件
        file_path = 'output/socks5_w_2.txt'
        # 验证信息
        with open(file_path,'r') as file:
            line_count = sum (1 for _ in file)
        print('---------------------------------------------------------')
        print(f'验证后的信息共计 {line_count} 行。已经保存到了:{file_path} ')
        print('---------------------------------------------------------')
        # 读取并且返回
        proxies = accuracy_2_socks5_run()
        if proxies is None:

            proxies = []
            return yanzhengcishu,proxies
        return yanzhengcishu,proxies,line_count
    except Exception as e :
        print('小问题,不要慌')
        proxies = []
        return yanzhengcishu,proxies,line_count
    return

# 获取数据并输出2
def accuracy_2_socks5_run():
    """读取 output/socks5_w_2.txt 文件并返回内容作为列表"""
    try:
        with open('output/socks5_w_2.txt', 'r') as file:
            # 读取所有行并去掉空行
            lines = file.readlines()
            # 移除每行末尾的换行符，并返回一个列表
            return [line.strip() for line in lines if line.strip()]
    except FileNotFoundError:
        return None
"""
################################################################################
# 验证仨次socks5的代理获取模块                                                   #
#                                                                              #
################################################################################
"""
def accuracy_3_socks5():
    try:
        print()
        # 设置验证次数
        yanzhengcishu = 3
        proxies = None
        # 读取文件
        file_path = 'output/socks5_w_3.txt'
        # 验证信息
        with open(file_path,'r') as file:
            line_count = sum (1 for _ in file)
        print('---------------------------------------------------------')
        print(f'验证后的信息共计 {line_count} 行。已经保存到了:{file_path} ')
        print('---------------------------------------------------------')
        # 读取并且返回
        proxies = accuracy_3_socks5_run()
        if proxies is None:

            proxies = []
            return yanzhengcishu,proxies
        return yanzhengcishu,proxies,line_count
    except Exception as e :
        print('小问题,不要慌')
        proxies = []
        return yanzhengcishu,proxies,line_count
    return

# 获取数据并输出3
def accuracy_3_socks5_run():
    """读取 output/socks5_w_3.txt 文件并返回内容作为列表"""
    try:
        with open('output/socks5_w_3.txt', 'r') as file:
            # 读取所有行并去掉空行
            lines = file.readlines()
            # 移除每行末尾的换行符，并返回一个列表
            return [line.strip() for line in lines if line.strip()]
    except FileNotFoundError:
        return None

"""
################################################################################
# 没验证的socks5的代理获取模块                                                   #
#                                                                              #
################################################################################
"""
def accuracy_4_socks5():
    try:
        print()
        # 设置验证次数
        yanzhengcishu = 0
        proxies = None
        # 读取文件
        file_path = 'output/socks5_v.txt'
        # 验证信息
        with open(file_path,'r') as file:
            line_count = sum (1 for _ in file)
        print('---------------------------------------------------------')
        print(f'验证后的信息共计 {line_count} 行。已经保存到了:{file_path} ')
        print('---------------------------------------------------------')
        # 读取并且返回
        proxies = accuracy_4_socks5_run()
        if proxies is None:
            proxies = []
            return yanzhengcishu,proxies
        return yanzhengcishu,proxies,line_count
    except Exception as e :
        print('小问题,不要慌')
        proxies = []
        return yanzhengcishu,proxies,line_count
    return

# 获取数据并输出1
def accuracy_4_socks5_run():
    """读取 output/socks5_v.txt 文件并返回内容作为列表"""
    try:
        with open('output/socks5_v.txt', 'r') as file:
            # 读取所有行并去掉空行
            lines = file.readlines()
            # 移除每行末尾的换行符，并返回一个列表
            return [line.strip() for line in lines if line.strip()]
    except FileNotFoundError:
        return None
"""
################################################################################
# 数量功能模块                                                                  #
#                                                                              #
################################################################################
"""
import random

def shuliang_mokuai(quantity, raw_proxies, line_count):
    """从原始代理列表中随机抽取指定数量（不生成副本）
    
    Args:
        quantity (int/str): 请求数量
        raw_proxies (list): 原始代理列表，格式为 ["ip:port", ...]
        line_count (int): 原始代理总数（可忽略，与旧代码兼容）
    
    Returns:
        tuple: (随机代理列表, 实际抽取数量)
    """
    try:
        # 参数验证
        quantity = int(quantity)
        if quantity <= 0:
            print("⚠️ 错误: 数量必须大于0")
            return [], 0
        
        # 计算实际可抽取量
        max_available = len(raw_proxies)
        actual_quantity = min(quantity, max_available)
        
        if actual_quantity == 0:
            print("⚠️ 警告: 代理池为空")
            return [], 0
        
        # 核心算法：生成随机索引直接抽取
        indices = random.sample(range(max_available), actual_quantity)
        selected = [raw_proxies[i] for i in indices]
        
        print(f"✅ 成功 | 需求: {quantity} 实际: {actual_quantity}")
        return selected, actual_quantity
        
    except ValueError as e:
        print(f"‼️ 参数错误: 数量必须为整数 ({e})")
        return [], 0
    except Exception as e:
        print(f"‼️ 系统错误: {e}")
        return [], 0
    return

"""
################################################################################
# 免费版500个模块                                                               #
#                                                                              #
################################################################################
"""

def http_500():
    try:
        print()
        # 设置验证次数
        yanzhengcishu = 0
        proxies = None
        # 读取文件
        file_path = 'output/500_http.txt'
        # 验证信息
        with open(file_path,'r') as file:
            line_count = sum (1 for _ in file)
        # print('---------------------------------------------------------')
        print(f'获取代理池ip共:{line_count} 行 ')
        # print('---------------------------------------------------------')
        # 读取并且返回
        proxies = http_500_1n()
        if proxies is None:
            proxies = []
            return yanzhengcishu,proxies
        return yanzhengcishu,proxies,line_count
    except Exception as e :
        print('小问题,不要慌')
        proxies = ['小问题不要慌']
        return yanzhengcishu,proxies,line_count
    return

# 获取数据并输出1
def http_500_1n():
    # """读取 output/socks5_v.txt 文件并返回内容作为列表"""
    try:
        with open('output/500_http.txt', 'r') as file:
            # 读取所有行并去掉空行
            lines = file.readlines()
            # 移除每行末尾的换行符，并返回一个列表
            return [line.strip() for line in lines if line.strip()]
    except FileNotFoundError:
        return None
    
"""
################################################################################
# 免费版500个socks5模块                                                         #
#                                                                              #
################################################################################
"""
def socks5_500():
    try:
        print()
        # 设置验证次数
        yanzhengcishu = 0
        proxies = None
        # 读取文件
        file_path = 'output/500_socks5.txt'
        # 验证信息
        with open(file_path,'r') as file:
            line_count = sum (1 for _ in file)
        print('---------------------------------------------------------')
        print(f'验证后的信息共计 {line_count} 行。已经保存到了:{file_path} ')
        print('---------------------------------------------------------')
        # 读取并且返回
        proxies = socks5_500_1n()
        if proxies is None:
            proxies = []
            return yanzhengcishu,proxies
        return yanzhengcishu,proxies,line_count
    except Exception as e :
        print('小问题,不要慌')
        proxies = ['小问题不要慌']
        return yanzhengcishu,proxies,line_count
    return

# 获取数据并输出1
def socks5_500_1n():
    # """读取 output/socks5_v.txt 文件并返回内容作为列表"""
    try:
        with open('output/500_socks5.txt', 'r') as file:
            # 读取所有行并去掉空行
            lines = file.readlines()
            # 移除每行末尾的换行符，并返回一个列表
            return [line.strip() for line in lines if line.strip()]
    except FileNotFoundError:
        return None