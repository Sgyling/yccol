import os
import requests
import uuid

fofa_key = ''
get_socks5='cHJvdG9jb2w9PSJzb2NrczUiICYmICJWZXJzaW9uOjUgTWV0aG9kOk5vIEF1dGhlbnRpY2F0aW9uKDB4MDApIiAmJiBhZnRlcj0iMjAyNC0xMi0yMCI%3D&full=ture&size=1000'

##############################################
version = 'V1.1'
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

get_http_url = f'https://fofa.info/api/v1/search/all?&key={fofa_key}&qbase64={get_http}&size=1000'
get_http_CN_url = f'https://fofa.info/api/v1/search/all?&key={fofa_key}&qbase64={get_http_CN}'
get_http_US_url = f'https://fofa.info/api/v1/search/all?&key={fofa_key}&qbase64={get_http_US}'
get_http_SG_url = f'https://fofa.info/api/v1/search/all?&key={fofa_key}&qbase64={get_http_SG}'
get_http_KR_url = f'https://fofa.info/api/v1/search/all?&key={fofa_key}&qbase64={get_http_KR}'
get_http_HK_url = f'https://fofa.info/api/v1/search/all?&key={fofa_key}&qbase64={get_http_HK}'

get_socks5_url = f'https://fofa.info/api/v1/search/all?&key={fofa_key}&qbase64={get_socks5}'
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

#获取mac地址
def get_mac_address():
    # 使用 uuid.getnode() 方法获取计算机的硬件地址
    mac_int = uuid.getnode()
    # 将整数形式的 MAC 地址转换为十六进制字符串，并以冒号分隔每两个字符
    mac_hex = ':'.join(("%012X" % mac_int)[i:i+2] for i in range(0, 12, 2))
    return mac_hex

#验证key
