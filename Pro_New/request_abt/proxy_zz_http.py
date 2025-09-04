import asyncio
import time
import sys
import os

# 代理转发函数
async def handle_connection(reader, writer):
    try:
        # 从客户端读取请求的目标地址和端口
        # 这里简化处理，假设直接使用当前的目标代理
        proxy_ip, proxy_port = current_proxy.split(':')
        # 连接到目标代理
        proxy_reader, proxy_writer = await asyncio.open_connection(proxy_ip, int(proxy_port))
        # 转发数据
        await asyncio.gather(
            forward(reader, proxy_writer),
            forward(proxy_reader, writer)
        )
    except Exception as e:
        print(f"代理转发出错: {e}")
    finally:
        writer.close()

# 数据转发函数
async def forward(reader, writer):
    try:
        while True:
            data = await reader.read(4096)
            if not data:
                break
            writer.write(data)
            await writer.drain()
    except Exception as e:
        print(f"数据转发出错: {e}")
    finally:
        writer.close()

# 主函数
async def main():
    global current_proxy
    try:
        config_file_path = os.path.join('config', 'conf.txt')
        with open(config_file_path, 'r', encoding='utf-8') as file:
            get_time = None
            local_port = None
            for line in file:
                line = line.strip()
                if line.startswith('get_time='):
                    value_part = line.split('=')[1]
                    get_time = value_part.strip("'")
                    print(f"ip切换时间为: {get_time}")
                elif line.startswith('local_port='):
                    value_part = line.split('=')[1]
                    local_port = int(value_part.strip("'"))
                    print(f"端口号为: {local_port}")
            if get_time is None or local_port is None:
                print("未在配置文件中找到 get_time 或 local_port 参数。")
                return

        with open('output/http.txt', 'r') as file:
            proxies = file.read().splitlines()
        if not proxies:
            print("代理文件为空，请检查 http.txt 文件。")
            return
        index = 0

        # 启动本地代理服务器
        server = await asyncio.start_server(handle_connection, '127.0.0.1', local_port)
        async with server:
            while True:
                current_proxy = proxies[index]
                print(f"当前目标代理为: {current_proxy}")
                index = (index + 1) % len(proxies)
                await asyncio.sleep(float(get_time))
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    current_proxy = None
    asyncio.run(main())