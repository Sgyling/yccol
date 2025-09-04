import os
get_http='Z2V0IGFsbCBwcm94eSBmcm9tIHByb3h5IHBvb2w='
# get_socks5='''
# protocol=="socks5" && "Version:5 Method:No Authentication(0x00)" && after="2022-02-01" && country="CN"
# '''

# get_http_url = f'https://fofa.info/api/v1/search/all?&key=509418042bbfedf43d9b4eec347fa669&qbase64={get_http}'


# 定义配置文件路径
config_file_path = os.path.join('config', 'conf.txt')

try:
    # 打开配置文件并读取内容
    with open(config_file_path, 'r',encoding='utf-8') as file:
        lines = file.readlines()

    # 初始化 key 值
    get_key = None

    # 遍历每一行，查找 key= 开头的行
    for line in lines:
        if line.strip().startswith('key='):
            # 提取等号后面的参数值
            get_key = line.strip().split('=')[1].strip("'")
            break

    # 检查是否成功提取到 key 值
    if get_key is None:
        print("未在配置文件中找到有效的 key 值。")
    else:
        # 构建 URL
        get_http_url = f'https://fofa.info/api/v1/search/all?&key={get_key}&qbase64={get_http}'
        # print(f"构建的 URL 为: {get_http_url}")

except FileNotFoundError:
    print(f"未找到配置文件: {config_file_path}")
except Exception as e:
    print(f"发生错误: {e}")
