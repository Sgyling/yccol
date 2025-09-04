import requests

# 请求API,获取原始数据
def get_ip_1(key):
    try:
        print('')
        url = f'http://api.Yccol.cc:3751/api/users?key={key}&proxy=http&area=all'
        response = requests.get(url)
        # print()
        response.raise_for_status()
        # 读取json数据
        data = response.json()

        if 'proxies' in data and isinstance(data['proxies'], list):
            proxies = data['proxies']
            # 将每个代理地址按行连接成一个字符串
            proxies_text = '\n'.join(proxies)
            # 将代理地址填充到文本框中
            # self.text_yanzheng.setPlainText(proxies_text)
            if '代理个数' in data:
                shuliang = str(data['代理个数'])
            else:
                shuliang = "未获取到代理个数信息"
            return proxies_text,shuliang
        else:
            # print("返回数据中没有 'proxies' 字段或者它不是一个列表。")
            # self.text_yanzheng.setPlainText("未找到有效的代理 IP 列表。")
            return '获取数据失败'
    except requests.RequestException as e:
        # print(f"请求出错: {e}")
        # self.text_yanzheng.setPlainText(f"请求出错: {e}")
        return '请求出错,请检查网络'
    except ValueError as e:
        # print(f"解析 JSON 数据出错: {e}")
        # self.text_yanzheng.setPlainText(f"解析 JSON 数据出错: {e}")
        return '解析输出错误'


