import requests
import random

# 目标网站
# target_url = "http://example.com"  # 请替换为实际的目标网站

# # 代理文件路径
# proxy_file = "output/http.txt"
# # 字典文件路径
# dict_file = "output/zidian/web_path_big.txt"

def load_proxies(file_path):
    """
    从文件中加载代理列表
    """
    proxies = []
    try:
        with open(file_path, 'r') as f:
            for line in f:
                proxy = line.strip()
                if proxy:
                    proxies.append({'http': proxy, 'https': proxy})
    except FileNotFoundError:
        print(f"代理文件 {file_path} 未找到。")
    return proxies

def load_dictionary(file_path):
    """
    从文件中加载扫描字典
    """
    paths = []
    try:
        with open(file_path, 'r') as f:
            for line in f:
                path = line.strip()
                if path:
                    paths.append(path)
    except FileNotFoundError:
        print(f"字典文件 {file_path} 未找到。")
    return paths

def scan_directory(url, path, proxy):
    """
    扫描单个目录
    """
    full_url = url.rstrip('/') + '/' + path.lstrip('/')
    try:
        response = requests.get(full_url, proxies=proxy, timeout=5)
        if response.status_code == 200:
            print(f"发现有效目录: {full_url}")
    except requests.RequestException as e:
        pass

def main(target_url,proxy_file,dict_file):
    # 加载代理和字典
    proxies = load_proxies(proxy_file)
    paths = load_dictionary(dict_file)

    if not proxies or not paths:
        return

    for path in paths:
        # 随机选择一个代理
        proxy = random.choice(proxies)
        scan_directory(target_url, path, proxy)

if __name__ == "__main__":
    main()