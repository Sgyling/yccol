import os
import requests
import uuid

fofa_key = ''
##############################################
version = 'V1.0'
yanzheng = ''
get_http='Z2V0IGFsbCBwcm94eSBmcm9tIHByb3h5IHBvb2w='
get_http_CN='Ym9keT0iZ2V0IGFsbCBwcm94eSBmcm9tIHByb3h5IHBvb2wiICYmIGNvdW50cnk9IkNOIg=='
get_http_US='m9keT0iZ2V0IGFsbCBwcm94eSBmcm9tIHByb3h5IHBvb2wiICYmIGNvdW50cnk9IlVTIg=='
# 新加坡
get_http_SG='Ym9keT0iZ2V0IGFsbCBwcm94eSBmcm9tIHByb3h5IHBvb2wiICYmIGNvdW50cnk9IlNHIg=='
# 韩国
get_http_KR='Ym9keT0iZ2V0IGFsbCBwcm94eSBmcm9tIHByb3h5IHBvb2wiICYmIGNvdW50cnk9IktSIg=='
# 香港
get_http_HK='Ym9keT0iZ2V0IGFsbCBwcm94eSBmcm9tIHByb3h5IHBvb2wiICYmIHJlZ2lvbj0iSEsi'
# get_socks5='''
# protocol=="socks5" && "Version:5 Method:No Authentication(0x00)" && after="2022-02-01" && country="CN"
# '''

get_http_url = f'https://fofa.info/api/v1/search/all?&key={fofa_key}&qbase64={get_http}'
get_http_CN_url = f'https://fofa.info/api/v1/search/all?&key={fofa_key}&qbase64={get_http_CN}'
get_http_US_url = f'https://fofa.info/api/v1/search/all?&key={fofa_key}&qbase64={get_http_US}'
get_http_SG_url = f'https://fofa.info/api/v1/search/all?&key={fofa_key}&qbase64={get_http_SG}'
get_http_KR_url = f'https://fofa.info/api/v1/search/all?&key={fofa_key}&qbase64={get_http_KR}'
get_http_HK_url = f'https://fofa.info/api/v1/search/all?&key={fofa_key}&qbase64={get_http_HK}'

def ip_sulv(ip_su):
        config_file_path = 'config/conf.txt'
        if not os.path.exists(os.path.dirname(config_file_path)):
            os.makedirs(os.path.dirname(config_file_path))
        try:
            # 读取配置文件内容
            with open(config_file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
            # 查找并更新 get_time 的值
            for i, line in enumerate(lines):
                if line.strip().startswith('get_time='):
                    lines[i] = f"get_time='{ip_su}'\n"
                    break
            else:
                # 如果没有找到 get_time 行，则添加新行
                lines.append(f"get_time='{ip_su}'\n")
            # 将更新后的内容写回到配置文件中
            with open(config_file_path, 'w', encoding='utf-8') as file:
                file.writelines(lines)
            print(f"配置文件已更新，get_time 的值已设置为 {ip_su}")
        except FileNotFoundError:
            print(f"未找到配置文件 {config_file_path}，将创建新文件并设置 get_time 的值。")
            with open(config_file_path, 'w', encoding='utf-8') as file:
                file.write(f"get_time='{ip_su}'\n")
            print(f"配置文件已创建，get_time 的值已设置为 {ip_su}")
        except Exception as e:
            print(f"更新配置文件时出现错误: {e}")
        return

def ban_ben_yanzheng():
    ban_ben_url = 'http://107.148.66.81/api/6K8t4X3qHdL95BjN6pWfY7zrQ20gJm3Ck5F8s7.txt'
    try:
        response = requests.get(ban_ben_url)
        response.raise_for_status()
        data = response.text
        print('最新版为:',data,'版本')
        print('当前版本为:',version)
        if version == data:
            print('--------------------------------\n当前已经是最新版本,无需更新\n--------------------------------')
        else:
            print('--------------------------------\n当前并非最新版\n准备更新中...\n--------------------------------')
            down_fifa0()
    except requests.exceptions.RequestException as e:
        print('无法链接服务器,请检查网络')

    return

def down_fifa0():
    url = 'http://107.148.66.81/api/fifa0-pro.exe'
    save_path = 'fifa0-pro.exe'
    try:
        # 发送 GET 请求
        response = requests.get(url, stream=True)
        # 检查请求是否成功
        response.raise_for_status()

        # 以二进制写入模式打开文件
        with open(save_path, 'wb') as file:
            # 分块写入文件，避免一次性加载大文件到内存中
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
        # print(f"文件下载成功，保存路径: {save_path}")
        print('--------------------------------\n主程序更新完成\n即将更新副程序\n--------------------------------')
        pei_zhi()
        print('--------------------------------\n更新完成,可以使用了!\n--------------------------------')
    except requests.exceptions.RequestException as e:
        print(f"更新错误!出现网络错误: {e}")
    except Exception as e:
        print(f"更新错误,请联系软件软件管理员: {e}")
    return

def pei_zhi():
    # 检测 config/conf.txt 文件是否存在
    config_dir = 'config'
    config_file_path = os.path.join(config_dir, 'conf.txt')

    # 检查 config 目录是否存在，不存在则创建
    if not os.path.exists(config_dir):
        os.makedirs(config_dir)

    # 检查 config/conf.txt 文件是否存在，不存在则创建并写入内容
    if not os.path.exists(config_file_path):
        with open(config_file_path, 'w') as f:
            f.write("get_time='0.2'")
        print(f"第二部分更新完成")
    else:
        print(f"第二部分无需更新")

    # 检测 output/proxy.txt 和 output/http.txt 文件是否存在
    output_dir = 'output'
    proxy_file_path = os.path.join(output_dir, 'proxy.txt')
    http_file_path = os.path.join(output_dir, 'http.txt')

    # 检查 output 目录是否存在，不存在则创建
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 检查 proxy.txt 文件
    if os.path.exists(proxy_file_path):
        print(f"")
    else:
        with open(proxy_file_path, 'w'):
            pass
        print(f"")

    # 检查 http.txt 文件
    if os.path.exists(http_file_path):
        print(f"")
    else:
        with open(http_file_path, 'w'):
            pass
        print(f"")
    return

#获取mac地址
def get_mac_address():
    # 使用 uuid.getnode() 方法获取计算机的硬件地址
    mac_int = uuid.getnode()
    # 将整数形式的 MAC 地址转换为十六进制字符串，并以冒号分隔每两个字符
    mac_hex = ':'.join(("%012X" % mac_int)[i:i+2] for i in range(0, 12, 2))
    return mac_hex

#验证key
