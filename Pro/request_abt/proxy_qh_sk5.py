import time
import winreg
import sys
import os

def set_proxy(proxy):
    try:
        # 打开 Internet 设置注册表项
        reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                 r'Software\Microsoft\Windows\CurrentVersion\Internet Settings',
                                 0, winreg.KEY_ALL_ACCESS)
        # 设置代理启用标志
        winreg.SetValueEx(reg_key, 'ProxyEnable', 0, winreg.REG_DWORD, 1)
        # 设置代理服务器地址，指定为 Socks5 代理
        winreg.SetValueEx(reg_key, 'ProxyServer', 0, winreg.REG_SZ, f'socks= {proxy}')
        winreg.CloseKey(reg_key)
        print('---------------------------------------------------------')
        print(f"当前 Socks5 代理为: {proxy}")
        print('---------------------------------------------------------')
    except Exception as e:
        print(f"设置代理时出错: {e}")

def disable_proxy():
    try:
        # 打开 Internet 设置注册表项
        reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                 r'Software\Microsoft\Windows\CurrentVersion\Internet Settings',
                                 0, winreg.KEY_ALL_ACCESS)
        # 禁用代理
        winreg.SetValueEx(reg_key, 'ProxyEnable', 0, winreg.REG_DWORD, 0)
        winreg.CloseKey(reg_key)
        print("代理已关闭")
    except Exception as e:
        print(f"关闭代理时出错: {e}")

def main():
    try:
        config_file_path = os.path.join('config', 'conf.txt')
        # 以只读模式打开文件
        with open(config_file_path, 'r', encoding='utf-8') as file:
            for line in file:
                # 去除行首尾的空白字符
                line = line.strip()
                if line.startswith('get_time='):
                    # 提取等号后面的部分
                    value_part = line.split('=')[1]
                    # 去除引号
                    get_time = value_part.strip("'")
                    print(f"get_time 的值为: {get_time}")
                    break
            else:
                print("未在配置文件中找到 get_time 参数。")
        # 读取 Socks5 代理文件
        with open('output/socks5_w.txt', 'r') as file:
            proxies = file.read().splitlines()
        if not proxies:
            print("代理文件为空，请检查 socks5.txt 文件。")
            return
        index = 0
        while True:
            proxy = proxies[index]
            set_proxy(proxy)
            index = (index + 1) % len(proxies)
            time.sleep(float(get_time))
    except KeyboardInterrupt:
        disable_proxy()
        sys.exit(0)
    except Exception as e:
        print(f"发生错误: {e}")
        disable_proxy()

if __name__ == "__main__":
    main()