# -*- coding: utf-8 -*-
import os
import json
import re
import requests
from requests.exceptions import HTTPError, JSONDecodeError

def read_config():
    """读取配置文件获取key和mac_id"""
    config_path = "config/conf.txt"
    
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"配置文件 {config_path} 不存在")

    # 修改这里：添加encoding参数
    with open(config_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 使用正则表达式匹配配置
    key_match = re.search(r"key\s*=\s*'(.*?)'", content)
    mac_match = re.search(r"mac_id\s*=\s*'(.*?)'", content)

    if not key_match:
        raise ValueError("配置文件中未找到有效的key")
    if not mac_match:
        raise ValueError("配置文件中未找到有效的mac_id")

    return key_match.group(1), mac_match.group(1)

def save_proxies(proxies):
    """保存代理列表到文件"""
    output_dir = "output"
    output_path = os.path.join(output_dir, "proxy.txt")
    
    # 创建输出目录
    os.makedirs(output_dir, exist_ok=True)
    
    # 写入代理数据
    with open(output_path, 'w') as f:
        for proxy in proxies:
            f.write(proxy + "\n")
    print(f"成功保存 {len(proxies)} 个代理到 {output_path}")

def main():
    try:
        # 1. 读取配置文件
        key, mac_id = read_config()
        
        # 2. 构造请求URL
        url = f"http://localhost:5000/api/key?key={key}&mac_id={mac_id}&proxy=http&area=all"
        # url = f"http://49.232.127.250:3751/api/users?key={key}&proxy=http&area=all"
        # print(url)
        
        # 3. 发送GET请求
        response = requests.get(url, timeout=15)
        try:
            response.raise_for_status()
        except HTTPError as http_err:
            # 尝试解析错误响应体
            try:
                error_data = response.json()
                server_error = error_data.get('error', '未提供错误详情')
                print('未进行初始化')
                # print(f"HTTP错误 | 状态码 {response.status_code} | 错误类型: {type(http_err).__name__} | 服务端错误信息: {server_error}")
            except JSONDecodeError:
                print(f"HTTP错误 | 状态码 {response.status_code} | 原始响应内容: {response.text[:200]}...")
            return

        # 处理成功响应中的业务错误
        data = response.json()
        if "error" in data:
            raise ValueError(f"业务逻辑错误: {data['error']} [错误代码: {data.get('code','无')}]")
        # 4. 解析JSON数据
        data = response.json()
        if "proxies" not in data:
            raise ValueError("响应中缺少代理数据")
            
        # 5. 保存代理列表
        save_proxies(data["proxies"])
    except requests.Timeout:
        print("请求超时：服务器未在15秒内响应")
    except requests.ConnectionError:
        print("网络连接失败：请检查互联网连接")
    except json.JSONDecodeError:
        print(f"响应数据解析失败，原始内容：{response.text[:200]}...")
    except KeyError as e:
        print(f"数据格式异常：缺少必要字段 - {str(e)}")
    except Exception as e:
        print(f"未捕获的异常：{type(e).__name__} - {str(e)}")
    except Exception as e:
        a = """
        --------------
        # 设备未授权 #
        --------------
        """
        print(f"未捕获的异常：{type(e).__name__} - {str(e)}")

# if __name__ == "__main__":
#     main()