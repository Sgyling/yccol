import asyncio
import aiohttp
import os

# 验证代理是否可用
async def verify_proxy(proxy):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get('http://httpbin.org/ip', proxy=f'http://{proxy}', timeout=2) as response:
                if response.status == 200:
                    return True
    except Exception as e:
        print(f"代理 {proxy} 验证失败: {e}")
    return False

# 持续验证代理文件中的 IP
async def verify_proxies_file(file_path):
    if not os.path.exists(file_path):
        print(f"文件 {file_path} 不存在。")
        return
    while True:
        with open(file_path, 'r') as file:
            proxies = file.read().splitlines()
        total_proxies = len(proxies)
        valid_proxies = []
        index = 1
        for proxy in proxies:
            if await verify_proxy(proxy):
                valid_proxies.append(proxy)
                print(f"当前验证条数: {index} 条，共计: {total_proxies} 条，验证成功: {proxy}")
            else:
                print(f"当前验证条数: {index} 条，共计: {total_proxies - 1} 条，验证失败: {proxy}，已删除")
                total_proxies -= 1
            index += 1

        # 将验证通过的代理写回文件
        with open(file_path, 'w') as file:
            for proxy in valid_proxies:
                file.write(proxy + '\n')
        print(f"验证完成，剩余有效代理数量: {len(valid_proxies)}")

# if __name__ == "__main__":
#     file_path = 'output/http.txt'
#     try:
#         asyncio.run(verify_proxies_file(file_path))
#     except KeyboardInterrupt:
#         print("程序已手动停止。")