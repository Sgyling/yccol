import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
import time
import os
import json

# 全局配置
BASE_DIR = 'output/diqu'
CN_FILE = os.path.join(BASE_DIR, 'cn.txt')
HTTP_PLUS = os.path.join(BASE_DIR, 'cn_http_90+.txt')
HTTP_MINUS = os.path.join(BASE_DIR, 'cn_http_90-.txt')
HTTPS_PLUS = os.path.join(BASE_DIR, 'cn_https_90+.txt')
HTTPS_MINUS = os.path.join(BASE_DIR, 'cn_https_90-.txt')
CHECK_URLS = {
    'http': 'http://httpbin.org/ip',
    'https': 'https://httpbin.org/ip'  # HTTPS验证地址
}
TIMEOUT = 5
THREADS = 100
CHECK_INTERVAL = 10
MIN_CHECKS = 10

# 全局状态跟踪
proxy_history = {}

def load_proxies():
    """加载并去重代理列表"""
    try:
        with open(CN_FILE, 'r') as f:
            return list({line.strip() for line in f if line.strip()})
    except Exception as e:
        print(f"⚠️ 代理加载错误: {str(e)}")
        return []

def verify_proxy(proxy):
    """双协议验证函数"""
    results = {'http': False, 'https': False}
    
    # 验证HTTP
    try:
        response = requests.get(
            CHECK_URLS['http'],
            proxies={'http': f'http://{proxy}'},
            timeout=TIMEOUT,
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        if response.status_code == 200:
            origin_ip = json.loads(response.text).get('origin', '')
            proxy_ip = proxy.split(':')[0]
            results['http'] = (origin_ip == proxy_ip)
    except:
        pass
    
    # 验证HTTPS
    try:
        response = requests.get(
            CHECK_URLS['https'],
            proxies={'https': f'http://{proxy}'},  # 注意这里使用http协议连接HTTPS代理
            timeout=TIMEOUT,
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        if response.status_code == 200:
            origin_ip = json.loads(response.text).get('origin', '')
            proxy_ip = proxy.split(':')[0]
            results['https'] = (origin_ip == proxy_ip)
    except:
        pass
    
    return (proxy, results['http'], results['https'])

def update_classification(protocol):
    """更新指定协议的分类文件"""
    plus_file = HTTP_PLUS if protocol == 'http' else HTTPS_PLUS
    minus_file = HTTP_MINUS if protocol == 'http' else HTTPS_MINUS
    
    valid_proxies = []
    invalid_proxies = []
    
    # 遍历所有已知代理
    for proxy in proxy_history:
        stats = proxy_history[proxy].get(protocol, {'success': 0, 'total': 0})
        if stats['total'] >= MIN_CHECKS:
            survival_rate = (stats['success'] / stats['total']) * 100
            if survival_rate >= 90:
                valid_proxies.append(proxy)
            else:
                invalid_proxies.append(proxy)
    
    # 写入文件
    with open(plus_file, 'w') as f:
        f.write('\n'.join(valid_proxies))
    with open(minus_file, 'w') as f:
        f.write('\n'.join(invalid_proxies))
    
    return len(valid_proxies), len(invalid_proxies)

def main():
    verification_round = 0
    os.makedirs(BASE_DIR, exist_ok=True)

    while True:
        verification_round += 1
        current_proxies = load_proxies()
        
        if not current_proxies:
            print(f"⏳ 轮次 {verification_round}: 无可用代理，跳过验证")
            time.sleep(CHECK_INTERVAL)
            continue
        
        # 多线程验证
        print(f"\n🔍 轮次 {verification_round} 验证 {len(current_proxies)} 个代理")
        results = []
        with ThreadPoolExecutor(max_workers=THREADS) as executor:
            futures = [executor.submit(verify_proxy, p) for p in current_proxies]
            with tqdm(total=len(futures), desc="验证进度", unit="proxy") as pbar:
                for future in as_completed(futures):
                    proxy, http_valid, https_valid = future.result()
                    results.append((proxy, http_valid, https_valid))
                    pbar.update(1)
        
        # 更新历史记录
        for proxy, http_valid, https_valid in results:
            if proxy not in proxy_history:
                proxy_history[proxy] = {
                    'http': {'success': 0, 'total': 0},
                    'https': {'success': 0, 'total': 0}
                }
            
            # 更新HTTP统计
            proxy_history[proxy]['http']['total'] += 1
            proxy_history[proxy]['http']['success'] += int(http_valid)
            
            # 更新HTTPS统计
            proxy_history[proxy]['https']['total'] += 1
            proxy_history[proxy]['https']['success'] += int(https_valid)
        
        # 存活率分类（从第10次验证开始）
        if verification_round >= 10:
            http_valid_count, http_invalid_count = update_classification('http')
            https_valid_count, https_invalid_count = update_classification('https')
            
            # 打印统计信息
            current_http_success = sum(1 for _, h, _ in results if h)
            current_https_success = sum(1 for _, _, h in results if h)
            print(f"\n📊 验证统计：")
            print(f"HTTP 本次成功率: {current_http_success}/{len(results)} ({current_http_success/len(results):.1%})")
            print(f"HTTPS 本次成功率: {current_https_success}/{len(results)} ({current_https_success/len(results):.1%})")
            print(f"HTTP 历史分类: {http_valid_count} 有效 | {http_invalid_count} 无效")
            print(f"HTTPS 历史分类: {https_valid_count} 有效 | {https_invalid_count} 无效")
            print(f"文件路径：\n- HTTP: {HTTP_PLUS}\n- HTTPS: {HTTPS_PLUS}")

        # 等待下一轮
        print(f"\n⏲️ 下次验证 {time.strftime('%H:%M:%S', time.localtime(time.time()+CHECK_INTERVAL))}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()