import os
import requests
import uuid
import re
##############################################
version = 'V1.3.1'
yanzheng = ''

# 设置git_time 功能
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

# 设置 local_port 功能
def prot_sulv(ip_su):
        config_file_path = 'config/conf.txt'
        if not os.path.exists(os.path.dirname(config_file_path)):
            os.makedirs(os.path.dirname(config_file_path))
        try:
            # 读取配置文件内容
            with open(config_file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
            # 查找并更新 get_time 的值
            for i, line in enumerate(lines):
                if line.strip().startswith('local_port='):
                    lines[i] = f"local_port='{ip_su}'\n"
                    break
            else:
                # 如果没有找到 get_time 行，则添加新行
                lines.append(f"local_port='{ip_su}'\n")
            # 将更新后的内容写回到配置文件中
            with open(config_file_path, 'w', encoding='utf-8') as file:
                file.writelines(lines)
            print(f"配置文件已更新，local_port 的值已设置为 {ip_su}")
        except FileNotFoundError:
            print(f"未找到配置文件 {config_file_path}，将创建新文件并设置 local_port 的值。")
            with open(config_file_path, 'w', encoding='utf-8') as file:
                file.write(f"local_port='{ip_su}'\n")
            print(f"配置文件已创建，local_port 的值已设置为 {ip_su}")
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

#初始化功能
def key_initialize(key):
    mac = get_mac_address()
    config_dir = 'config'
    config_file = os.path.join(config_dir,'conf.txt')
    os.makedirs(config_dir, exist_ok=True)

    lines = []
    # 读取文件
    if os.path.exists(config_file):
        with open(config_file,'r',encoding='utf-8') as f:
            lines = f.readlines()
        #正则表达获取信息
        key_re = re.compile(r'^\s*key\s*=')
        mac_id_re = re.compile(r'^\s*mac_id\s*=')
        key_found = False 
        mac_found = False
        # 遍历并更新key or mac_id
        for i in range(len(lines)):
            line = lines[i].strip()
            if key_re.match(line):
                lines[i] = f"key='{key}'\n"
                key_found = True
            elif mac_id_re.match(line):
                lines[i] = f"mac_id='{mac.replace(':','')}'\n"
                mac_found = True
            # 添加缺失的条目
        if not key_found:
            lines.append(f"key='{key}'\n")
        if not mac_found:
            lines.append(f"mac_id='{mac.replace(':','')}'\n")
        
        # 写入配置文件
        with open(config_file, 'w', encoding='utf-8') as f:
            f.writelines(lines)
        
        # print(f"初始化成功！密钥和MAC地址已保存至 {config_file}")
        a = """
        --------------
        # 初始化成功 #
        --------------
        """
        return a
    
    else :
        return '初始化遇到问题,请手动添加config/config.txt文件'
    
    return '初始化遇到非常大的问题,请联系开发者:Yancy_76(B站:疯狂的杨CC)'
