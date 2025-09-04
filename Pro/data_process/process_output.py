import json
import requests
# from tomlkit import item

ip_list = []
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
            # print(f'{ip_data}当前状态码为:,{response.status_code},获取中...')
            if response.status_code == 200:
                print('---------------------------------------------------------')
                print(f'{ip_data}当前状态码为:,{response.status_code},获取中...')
                print('---------------------------------------------------------\n')
                html = response.text
                # print(ip_data,'获取中...')
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
            else :
                print('---------------------------------------------------------')
                print(f'{ip_data}当前状态码为:,{response.status_code},已跳过')
                print('---------------------------------------------------------\n')
        except requests.RequestException as req_err:
            print('---------------------------------------------------------')
            print(f"请求 {ip_data} 时发生网络请求错误,跳过该 IP，继续处理下一个。")
            print('---------------------------------------------------------\n')
        except json.JSONDecodeError as json_err:
            print('---------------------------------------------------------')
            print(f"解析 {ip_data} 返回的 JSON 数据时出错,跳过该 IP，继续处理下一个。")
            print('---------------------------------------------------------\n')
        except KeyError as key_err:
            print('---------------------------------------------------------')
            print(f"在处理 {ip_data} 返回的数据时，未找到所需的键，跳过该 IP，继续处理下一个。")
            print('---------------------------------------------------------\n')
        except Exception as e:
            # import traceback
            print('---------------------------------------------------------')
            print(f"处理 {ip_data} 时发生未知错误,跳过该 IP 源，继续处理下一个。")
            print('---------------------------------------------------------\n')
            # traceback.print_exc()
            # print("跳过该 IP 源，继续处理下一个。")
    # print(f"数据已保存到 {file_path} 文件中。\n--- 可以开始验证了~ ---")
        # 统计文件行数
    with open('output/proxy.txt', 'r') as file:
        line_count = sum(1 for _ in file)
    print('---------------------------------------------------------')
    print(f'代理信息共有 {line_count} 条。已经保存到了: output/proxy.txt,可以使用了')
    print('---------------------------------------------------------\n')
    return
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
        print('---------------------------------------------------------')
        print(f'未验证代理信息共有 {line_count} 行。已经保存到了:{file_path} 可以准备验证咯~')
        print('---------------------------------------------------------')
    except Exception as e:
        print(f'有点小错误:{e}')
    return
# 去重
def qu_chong(path):
    try:
        # 以读取模式打开文件
        with open(path, 'r', encoding='utf-8') as file:
            # 读取文件的每一行，并去除行尾的换行符
            lines = [line.strip() for line in file.readlines()]

        # 使用集合去重，集合的元素具有唯一性
        unique_lines = set(lines)

        # 以写入模式打开文件，将去重后的内容写回文件
        with open(path, 'w', encoding='utf-8') as file:
            # 遍历去重后的集合
            for line in unique_lines:
                # 将每一行内容写入文件，并添加换行符
                file.write(line + '\n')

        # 再次以读取模式打开文件，统计行数
        with open(path, 'r', encoding='utf-8') as file:
            line_count = sum(1 for _ in file)

        print(f"去重完成，已将结果保存到 {path} 文件中。去重后共{line_count}条代理池.")
    except FileNotFoundError:
        print(f"未找到 {path} 文件，请检查文件路径。")
    except Exception as e:
        print(f"发生错误: {e}")