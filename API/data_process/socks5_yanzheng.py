import socks
import socket

def verify_socks5_proxy(proxy):
    try:
        ip, port = proxy.split(':')
        port = int(port)

        # 设置 SOCKS5 代理
        socks.set_default_proxy(socks.SOCKS5, ip, port)
        socket.socket = socks.socksocket  # 替换默认的 socket 对象为 socks 的版本

        # 测试代理是否有效，尝试连接一个网站
        socket.create_connection(('www.google.com', 80), timeout=1)
        print(f"代理 {proxy} 验证成功")
        return proxy
    except Exception as e:
        print(f"代理 {proxy} 验证失败，原因: {str(e)}")
        return None

def check_proxies_from_file(input_file, output_file):
    with open(input_file, 'r') as file:
        proxies = file.readlines()
    total_proxies = len(proxies)

    successful_proxies = []

    for index, proxy in enumerate(proxies, start=1):
        proxy = proxy.strip()
        print(f"------------------------------------------正在验证第 {index} 个代理，总共 {total_proxies} 个代理")
        result = verify_socks5_proxy(proxy)
        if result:
            successful_proxies.append(result)

    # 将验证成功的代理写入输出文件
    with open(output_file, 'w') as file:
        for proxy in successful_proxies:
            file.write(proxy + '\n')
    print(f"\n验证成功的代理已保存到 {output_file}")

def socks5_yz():
    # 调用函数，验证 socks5_v.txt 中的所有代理，并将验证通过的代理保存到 socks5_w.txt
    check_proxies_from_file('output/socks5_v.txt', 'output/socks5_w.txt')

    # 统计文件行数
    with open('output/socks5_w.txt', 'r') as file:
        line_count = sum(1 for _ in file)
    print(f'\n验证成功的代理信息共有 {line_count} 行。已经保存到了: output/socks5_w.txt,可以使用了')
    return

def socks5_yz_2():
    # 调用函数，验证 socks5_v.txt 中的所有代理，并将验证通过的代理保存到 socks5_w.txt
    check_proxies_from_file('output/socks5_w.txt', 'output/socks5_w_2.txt')

    # 统计文件行数
    with open('output/socks5_w_2.txt', 'r') as file:
        line_count = sum(1 for _ in file)
    print(f'\n验证成功的代理信息共有 {line_count} 行。已经保存到了: output/socks5_w_2.txt,可以使用了')
    return

def socks5_yz_3():
    # 调用函数，验证 socks5_v.txt 中的所有代理，并将验证通过的代理保存到 socks5_w.txt
    check_proxies_from_file('output/socks5_w_2.txt', 'output/socks5_w_3.txt')

    # 统计文件行数
    with open('output/socks5_w_3.txt', 'r') as file:
        line_count = sum(1 for _ in file)
    print(f'\n验证成功的代理信息共有 {line_count} 行。已经保存到了: output/socks5_w_2.txt,可以使用了')
    return
# 调用验证函数
# socks5_yz()