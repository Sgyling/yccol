import requests
import threading
from queue import Queue

def read_proxies_from_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"文件 '{filename}' 未找到。")
        return []

import requests
from requests.exceptions import RequestException

def test_proxies(proxies, test_url):
    working_proxies = []
    for proxy in proxies:
        proxy_dict = {
            "http": f"http://{proxy}",
            "https": f"http://{proxy}"
        }
        try:
            response = requests.get(test_url, proxies=proxy_dict, timeout=5)
            if response.status_code == 200:
                working_proxies.append(proxy)
        except RequestException:
            pass
    return working_proxies

def save_working_proxies(proxies, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for proxy in proxies:
            file.write(proxy + '\n')

def remove_duplicate_ips(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        unique_lines = list(set(lines))
        with open(filename, 'w', encoding='utf-8') as file:
            file.writelines(unique_lines)
        print(f"已对文件 '{filename}' 中的 IP 数据去重。")
    except FileNotFoundError:
        print(f"文件 '{filename}' 未找到，无法进行去重操作。")



# 从文件中读取代理列表
def read_proxies_from_file(filename):
    try:
        with open(filename, "r") as file:
            proxies = [line.strip() for line in file if line.strip()]
        return proxies
    except FileNotFoundError:
        print(f"未找到文件: {filename}，请检查文件是否存在。")
        return []

# 测试单个代理的可用性
def test_single_proxy(proxy, test_url, working_proxies_queue):
    try:
        response = requests.get(test_url, proxies={"http": proxy, "https": proxy}, timeout=5)
        if response.status_code == 200:
            # print(f"代理 {proxy} 可用，返回 IP: {response.json()['origin']}")
            working_proxies_queue.put(proxy)
        else:
            # print(f"代理 {proxy} 不可用")
            a = ''
    except Exception as e:
        # print(f"代理池验证出错,验证下一个")
        a = ''

# 测试代理的可用性（多线程）
def test_proxies(proxies, test_url):
    working_proxies_queue = Queue()
    threads = []

    # 为每个代理创建一个线程
    for proxy in proxies:
        thread = threading.Thread(target=test_single_proxy, args=(proxy, test_url, working_proxies_queue))
        threads.append(thread)
        thread.start()

    # 等待所有线程完成
    for thread in threads:
        thread.join()

    # 从队列中取出所有可用代理
    working_proxies = []
    while not working_proxies_queue.empty():
        working_proxies.append(working_proxies_queue.get())

    return working_proxies

# 将可用的代理保存到文件
def save_working_proxies(working_proxies, output_filename):
    with open(output_filename, "w") as file:
        for proxy in working_proxies:
            file.write(proxy + "\n")
    print(f"可用的代理已保存到 '{output_filename}'，共 {len(working_proxies)} 个。")

# 主函数
def main():
    # 输入文件和输出文件
    input_filename = "output/proxy.txt"
    output_filename = "output/http.txt"
    daili_geshu = ''
    # 测试 URL
    test_url = "http://httpbin.org/ip"

    # 读取代理列表
    proxies = read_proxies_from_file(input_filename)
    if not proxies:
        print(f"文件 '{input_filename}' 中没有找到有效的代理。")
        return

    print(f"从文件 '{input_filename}' 中读取到 {len(proxies)} 个代理，开始测试...")
    daili_geshu = len(proxies)
    # 测试代理
    working_proxies = test_proxies(proxies, test_url)

    # 保存可用的代理
    if working_proxies:
        save_working_proxies(working_proxies, output_filename)

    else:
        print("没有可用的代理。")
    
    return daili_geshu

# 二次验证
def main2():
    # 输入文件和输出文件
    input_filename = "output/http.txt"
    output_filename = "output/http2.txt"
    daili_geshu = ''
    # 测试 URL
    test_url = "http://httpbin.org/ip"

    # 读取代理列表
    proxies = read_proxies_from_file(input_filename)
    if not proxies:
        print(f"文件 '{input_filename}' 中没有找到有效的代理。")
        return

    print(f"从文件 '{input_filename}' 中读取到 {len(proxies)} 个代理，开始测试...")
    daili_geshu = len(proxies)
    # 测试代理
    working_proxies = test_proxies(proxies, test_url)

    # 保存可用的代理
    if working_proxies:
        save_working_proxies(working_proxies, output_filename)

    else:
        print("没有可用的代理。")
    
    return daili_geshu

# 三次验证
def main3():
    # 输入文件和输出文件
    input_filename = "output/http2.txt"
    output_filename = "output/http3.txt"
    daili_geshu = ''
    # 测试 URL
    test_url = "http://httpbin.org/ip"

    # 读取代理列表
    proxies = read_proxies_from_file(input_filename)
    if not proxies:
        print(f"文件 '{input_filename}' 中没有找到有效的代理。")
        return

    print(f"从文件 '{input_filename}' 中读取到 {len(proxies)} 个代理，开始测试...")
    daili_geshu = len(proxies)
    # 测试代理
    working_proxies = test_proxies(proxies, test_url)

    # 保存可用的代理
    if working_proxies:
        save_working_proxies(working_proxies, output_filename)
        # 对保存的文件进行去重操作
        remove_duplicate_ips(output_filename)
    else:
        print("没有可用的代理。")
    
    return daili_geshu




# # 验证中国的代理池ip
# def main_cn():
#     # 输入文件和输出文件
#     input_filename = "output/diqu/cn.txt"
#     output_filename = "output/diqu/diqu_w/cn.txt"
#     daili_geshu = ''
#     # 测试 URL
#     test_url = "http://httpbin.org/ip"

#     # 读取代理列表
#     proxies = read_proxies_from_file(input_filename)
#     if not proxies:
#         print(f"文件 '{input_filename}' 中没有找到有效的代理。")
#         return

#     print(f"从文件 '{input_filename}' 中读取到 {len(proxies)} 个代理，开始测试...")
#     daili_geshu = len(proxies)
#     # 测试代理
#     working_proxies = test_proxies(proxies, test_url)

#     # 保存可用的代理
#     if working_proxies:
#         save_working_proxies(working_proxies, output_filename)

#     else:
#         print("没有可用的代理。")
# if __name__ == "__main__":
#     main()