import requests
import json

# 发送请求
# with urllib.request.urlopen(url=config.config.get_http_url) as response:
#     html = response.read().decode('utf-8')
#     print(html)
def get_http():

    api_url = "http://api.Yancy77.cn:3751/api/v2/http"
    save_path = "output/proxy.txt"  # 保存文件名可自定义

    try:
        # 发送GET请求
        response = requests.get(api_url)
        response.raise_for_status()  # 自动检测HTTP错误
        
        # 解析JSON数据
        data = response.json()
        
        # 提取proxies字段内容（假设返回格式为 {"proxies": [...]}）
        proxies = data.get("proxies", [])
        
        if not proxies:
            print("警告：未找到有效代理数据")
        else:
            # 保存到文件（每行一个代理）
            with open(save_path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(proxies))
            
            print(f"成功保存 {len(proxies)} 条代理至 {save_path}")

    except requests.exceptions.RequestException as e:
        print(f"请求失败: {str(e)}")
    except json.JSONDecodeError:
        print("错误：返回数据不是有效JSON格式")
    except KeyError:
        print("错误：返回数据中缺少proxies字段")

    return response

def get_socks5():
        
    api_url = "http://api.Yccol.cc:3751/api/v2/socks5"
    save_path = "output/proxy.txt"  # 保存文件名可自定义

    try:
        # 发送GET请求
        response = requests.get(api_url)
        response.raise_for_status()  # 自动检测HTTP错误
        
        # 解析JSON数据
        data = response.json()
        
        # 提取proxies字段内容（假设返回格式为 {"proxies": [...]}）
        proxies = data.get("proxies", [])
        
        if not proxies:
            print("警告：未找到有效代理数据")
        else:
            # 保存到文件（每行一个代理）
            with open(save_path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(proxies))
            
            print(f"成功保存 {len(proxies)} 条代理至 {save_path}")

    except requests.exceptions.RequestException as e:
        print(f"请求失败: {str(e)}")
    except json.JSONDecodeError:
        print("错误：返回数据不是有效JSON格式")
    except KeyError:
        print("错误：返回数据中缺少proxies字段")



    return response