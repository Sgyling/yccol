import config.config
# import request_abt
# import request_abt
import proxy_qh
from request_abt import get_request
from output import http_yanzheng

# print(config.config.get_http_url)
a = f'''
 (·人·)~ 杨CC写的哈~
 B站up:疯狂的杨CC
 温馨提示:请在config/conf.txt中添加fofa的key
 再次温馨提示:只要注册登录fofa就有key哦~
 再再次提示:不需要fofa会员也可以用(只是功能受限)
 再再再次提示:此工具有收费版本,比免费版好用很多,而且不需要设置key,如果需要付费版本,请联系:QQ323002946或者微信:Yancy_76
 付费说明:源码100RMB,付费版180RMB,打包270RMB(付费版目前为买断制\包更新,加入粉丝群后付费仅需80RMB)
'''
print(a,'\n\n1:获取代理\n2:验证代理\n3:开启代理切换\n4:全自动操作(包含:获取代理\验证代理\代理切换)')
user_input = input('请输入上方所提示的数字:\n')

if user_input == '1':
    print('---当前选择使用的是http或https代理---')
    file_path = f"output/proxy.txt"
    with open(file_path, "w") as file:
        pass
    html = get_request.get_http()
    # print(html)
elif user_input =='2':
    print('--- 验证代理中 ---')
    http_yanzheng.main()
elif user_input == '3':
    print('--- 开启切换代理 ---\n')
    proxy_qh.main()
elif user_input =='4':
    file_path = f"output/proxy.txt"
    with open(file_path, "w") as file:
        pass
    print('--- 唉嘿~ 你选择全自动了哇~ ---')
    get_request.get_http()
    http_yanzheng.main()
    proxy_qh.main()
else:
    print('输入有误,如需退出,请直接CTRL+C 或 输入000')

