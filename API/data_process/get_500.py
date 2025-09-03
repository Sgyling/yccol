
def http_500():
    input_file = 'output/proxy.txt'
    output_file = 'output/500_http.txt'
    # 读取数据并提取前500条
    with open(input_file, 'r', encoding='utf-8') as f:
        # 读取所有行并截取前500条
        selected_data = [next(f) for _ in range(500)]  # 精确500条（文件不足时会报错）

    # 处理文件不足500行的情况（避免报错）
    # selected_data = []
    # with open(input_file, 'r', encoding='utf-8') as f:
    #     for i, line in enumerate(f):
    #         if i >= 500:
    #             break
    #         selected_data.append(line)

    # 写入新文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(selected_data)

def socks5_500():
    input_file = 'output/socks5_v.txt'
    output_file = 'output/500_socks5.txt'
    # 读取数据并提取前500条
    with open(input_file, 'r', encoding='utf-8') as f:
        # 读取所有行并截取前500条
        selected_data = [next(f) for _ in range(500)]  # 精确500条（文件不足时会报错）

    # 处理文件不足500行的情况（避免报错）
    # selected_data = []
    # with open(input_file, 'r', encoding='utf-8') as f:
    #     for i, line in enumerate(f):
    #         if i >= 500:
    #             break
    #         selected_data.append(line)

    # 写入新文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(selected_data)