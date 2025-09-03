import json
import requests
# from tomlkit import item

ip_list = []
# 先从返回数据中找到 数据,处理一下
def process_http(html):
    data = json.loads(html)

    for re in data["results"]:
        if len(re) >=3:
            ip = re[1]
            port = re[2]
            ip_port = f"{ip}:{port}"
            ip_list.append(ip_port)
            # print(ip_port)
        else:
            print('当前没有找到对应数据,正在进行下一个')
    return ip_list

# 这一块是处理fofa获取的数据
def process_http_fofa(html):

    for ip_data in ip_list:
        # print(ip_data)
        try:
            url = f'http://{ip_data}/all'
            response = requests.get(url,verify=False,timeout=10)
            if response.status_code == 200:
                print(f'{ip_data}当前状态码为:,{response.status_code}')
                html = response.text
                # print(html)
                parsed_data = json.loads(html)
                # proxy_data = parsed_data.get("proxy",[])
                proxy_data = [item["proxy"] for item in parsed_data]
                file_path = f"output/proxy.txt"
                # with open(file_path, "w") as file:
                #     pass
                with open(file_path,"a") as file:
                    pass
                    for data in proxy_data:
                        file.write(data + "\n")
        except requests.RequestException as req_err:
            print(f"请求 {ip_data} 时发生网络请求错误跳过该 IP，继续处理下一个。")
        except json.JSONDecodeError as json_err:
            print(f"解析 {ip_data} 返回的 JSON 数据时出错跳过该 IP，继续处理下一个。")
        except KeyError as key_err:
            print(f"在处理 {ip_data} 返回的数据时，未找到所需的键跳过该 IP，继续处理下一个。")
        except Exception as e:
            import traceback
            print(f"处理 {ip_data} 时发生未知错误: ")
            traceback.print_exc()
            print("跳过该 IP，继续处理下一个。")
    print(f"数据已保存到 {file_path} 文件中。\n--- 可以开始验证了~ ---")
    return ip_list
    # return ''

# socks5 代理池存储
def process_socks5_fofa(html):
    file_path = 'output/socks5_v.txt'

    import os
    os.makedirs(os.path.dirname(file_path),exist_ok=True)
    try:
        with open(file_path,'a') as file:
            for proxy in html :
                file.write(proxy + '\n')
                print('代理:',proxy,'已记录')
            # print(f'信息存储到了成功:{file_path}')
        # 统计文件行数
        with open(file_path, 'r') as file:
            line_count = sum(1 for _ in file)
        print(f'未验证代理信息共有 {line_count} 行。已经保存到了:{file_path} 可以准备验证咯~')
    except Exception as e:
        print(f'有点小错误:{e}')
    return