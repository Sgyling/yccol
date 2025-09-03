import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock
import time

# 配置区
INPUT_FILE = "output/diqu/proxy.txt"
OUTPUT_FILE = "output/diqu/cn_https.txt"
TEST_URL = "https://www.baidu.com"  # 更可靠的测试地址
TIMEOUT = 8
MAX_WORKERS = 80  # 根据网络状况调整
PRINT_LOCK = Lock()

def format_proxy(proxy_str):
    """标准化代理格式为http://ip:port"""
    proxy_str = proxy_str.strip()
    if proxy_str.startswith(('http://', 'https://')):
        return proxy_str
    return f"http://{proxy_str}"

def test_https_proxy(proxy):
    """测试代理的HTTPS支持"""
    proxies = {
        "https": proxy,  # 关键设置：使用http协议代理处理https请求
        "http": proxy
    }
    
    try:
        start = time.time()
        response = requests.get(
            TEST_URL,
            proxies=proxies,
            timeout=TIMEOUT,
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        latency = int((time.time() - start) * 1000)
        
        if response.status_code == 200:
            with PRINT_LOCK:
                print(f"✅ 有效代理 {proxy} 延迟{latency}ms")
            return True
    except requests.exceptions.ProxyError as pe:
        with PRINT_LOCK:
            print(f"❌ 代理错误 {proxy}: {str(pe).split('(')[0]}")
    except Exception as e:
        with PRINT_LOCK:
            print(f"⛔ 连接异常 {proxy}: {type(e).__name__}")
    return False

def main():
    print("🎯 开始HTTPS代理验证...")
    
    # 读取并格式化代理
    try:
        with open(INPUT_FILE, 'r') as f:
            raw_proxies = [line.strip() for line in f if line.strip()]
        proxies = [format_proxy(p) for p in raw_proxies]
        print(f"📥 已加载 {len(proxies)} 个代理")
    except FileNotFoundError:
        print(f"错误：文件 {INPUT_FILE} 不存在")
        return

    # 多线程验证
    valid_proxies = []
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {executor.submit(test_https_proxy, p): p for p in proxies}
        
        for future in as_completed(futures):
            proxy = futures[future]
            if future.result():
                valid_proxies.append(proxy)

    # 保存结果
    with open(OUTPUT_FILE, 'w') as f:
        f.write('\n'.join(valid_proxies))
    
    print(f"\n🎉 验证完成！有效代理 {len(valid_proxies)} 个")
    print(f"已保存至 {OUTPUT_FILE}")

if __name__ == "__main__":
    main()