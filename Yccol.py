from request_abt import get_request,proxy_zz_http
from output import http_yanzheng
import asyncio

# print(config.config.get_http_url)
a = f'''
------------------------------------------------------------------------------------------------------------------
 (·人·)~ 杨CC写的哈~
 B站up:疯狂的杨CC
 版本号:V1.3.0
 Yccol官网:https://yccol.cc
 Yccol教程:https://yccol.cc/Yccol-Help.html
 (*^▽^*) :当前版本支持Burp\指纹浏览器等场景使用了哦~(端口号请在config/conf.txt中进行修改哈)
 
------------------------------------------------------------------------------------------------------------------
'''
print(a,'\n\n1:获取http代理\n2:获取socks5代理\n3:验证http代理\n\n4.开启http中转代理\n\nn000.退出请直接CTRL+C 或 输入000')
user_input = input('请输入上方所提示的数字\n:')

if user_input == '1':
    print('--- 获取http代理池 ---')
    file_path = f"output/proxy.txt"
    with open(file_path, "w") as file:
        pass
    get_request.get_http()
    # print(html)
elif user_input =='2':
    print('--- 获取socks5代理池 ---')
    get_request.get_socks5()
elif user_input == '3':
    print('--- 验证http代理 ---\n')
    # proxy_qh.main()
    http_yanzheng.main()
    # asyncio.run(proxy_zz_http.main())

elif user_input == '4':
    # print('---当前选择使用的是http或https代理---')
    print('--------------------------------------\n开启成功,默认端口:33333\n--------------------------------------')
    asyncio.run(proxy_zz_http.main())
else:
    print('输入有误,如需退出,请直接CTRL+C 或 输入000')

