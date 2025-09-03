import os
import IP2Location
import socket
from collections import defaultdict

# 配置路径
PROXY_FILE = "output/proxy.txt"
DATABASE_FILE = "config/IP2LOCATION-LITE-DB3.BIN"
OUTPUT_DIR = "output/diqu"

# 初始化数据库
db = IP2Location.IP2Location()

def ensure_dir(path):
    """确保输出目录存在"""
    os.makedirs(path, exist_ok=True)

def validate_ip(ip):
    """验证IP格式有效性（支持IPv4/IPv6）"""
    try:
        socket.inet_pton(socket.AF_INET6 if ":" in ip else socket.AF_INET, ip)
        return True
    except socket.error:
        return False

def parse_proxy_file():
    """安全解析代理文件（保留端口）"""
    proxies = []
    with open(PROXY_FILE, "r") as f:
        for line in f:
            line = line.strip()
            if line.count(":") == 1:  # 简单分割IP:PORT
                ip_part, port = line.split(":", 1)
                if validate_ip(ip_part) and port.isdigit():
                    proxies.append(line)
                else:
                    print(f"忽略无效行: {line}")
            else:
                print(f"格式错误: {line}")
    return proxies

def classify_proxies(proxies):
    """增强型分类逻辑（仅分国内/国外）"""
    cn_proxies = []
    fcn_proxies = []
    
    for proxy in proxies:
        ip = proxy.split(":", 1)[0]  # 提取IP部分
        
        try:
            record = db.get_all(ip)
            if record.country_short == "CN":
                cn_proxies.append(proxy)
            else:
                fcn_proxies.append(proxy)
        except Exception as e:
            print(f"数据库查询失败 [{proxy}]: {str(e)}")
            fcn_proxies.append(proxy)  # 查询失败默认归类到国外
            
    return cn_proxies, fcn_proxies

def save_results(cn_list, fcn_list):
    """结构化保存结果"""
    ensure_dir(OUTPUT_DIR)
    
    cn_path = os.path.join(OUTPUT_DIR, "cn.txt")
    fcn_path = os.path.join(OUTPUT_DIR, "fcn.txt")
    
    with open(cn_path, "w") as f:
        f.write("\n".join(cn_list))
    with open(fcn_path, "w") as f:
        f.write("\n".join(fcn_list))
    
    print(f"✅ 国内代理已保存至 {cn_path} ({len(cn_list)}条)")
    print(f"✅ 国外代理已保存至 {fcn_path} ({len(fcn_list)}条)")

def main():
    """主流程控制"""
    try:
        db.open(DATABASE_FILE)
    except Exception as e:
        print(f"‼️ 数据库加载失败: {str(e)}")
        return
    
    print("🔄 开始处理代理数据...")
    proxies = parse_proxy_file()
    print(f"📊 共读取有效代理: {len(proxies)} 条")
    
    if not proxies:
        print("⚠️ 无有效代理数据，终止操作")
        return
    
    cn, fcn = classify_proxies(proxies)
    save_results(cn, fcn)
    print(f"\n🎉 分类完成 | 国内: {len(cn)}条 | 国外: {len(fcn)}条")

if __name__ == "__main__":
    main()