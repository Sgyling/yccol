import requests
import config.config
import data_process.process_output

# 发送请求
# with urllib.request.urlopen(url=config.config.get_http_url) as response:
#     html = response.read().decode('utf-8')
#     print(html)
def get_http(url):

    response = requests.get(url)
    if response.status_code == 200:
        html = response.text
        # print(html)
        htmla = data_process.process_output.process_http(html)
        htmlb =data_process.process_output.process_http_fofa(htmla)
        # print('开始验证获取到的ip')
        # output.http_yanzheng
        return htmlb

    else:
        print('出现错误,请检查网络')
        
# 处理socks5代理池
def get_socks5():
        
    response = requests.get(config.config.get_socks5_url)
    if response.status_code == 200:
        html = response.text
        # print(html)
        htmla = data_process.process_output.process_http(html)
        htmlb =data_process.process_output.process_socks5_fofa(htmla)
        # print('开始验证获取到的ip')
        # output.http_yanzheng
        return htmlb

    else:
        print('出现错误,请检查网络')
    return response


