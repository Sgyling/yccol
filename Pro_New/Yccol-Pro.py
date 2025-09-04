import config.config
import data_process.process_output
import data_process.socks5_yanzheng
from request_abt import proxy_qh,proxy_qh_sk5,proxy_zz_http,for_yan_zheng_http,get_http_0,get_socks5_0
from data_process import http_yanzheng,socks5_yanzheng
import config.config
import argparse
import asyncio
import ssl
import time



def main():
    par = argparse.ArgumentParser(usage="Yccol-Pro.exe [-h] [-f] [-vo] [-s] [-a] [-R] [-fi] [-fs] [-sy] [-sq] [-v]")

    par.add_argument("-f","--fofa_get_ip", action="store_true",dest="fofa_get_ip",
                      help="通过fofa获取ip")
    par.add_argument("-vo","--Ver_out_ip",action="store_true",dest="ver_out_ip",
                     help="验证ip")
    par.add_argument("-s","--switch_ip",action="store_true",dest="switch_ip",
                      help="开启切换ip功能")
    par.add_argument("-a","--Automatic_ip",action="store_true",dest="automatic_ip",
                      help="自动运行整套程序")
    par.add_argument("-fs","--get_socks5",action="store_true",dest="get_socks5",
                      help="获取socks5代理池(全球未指定地址)")
    par.add_argument("-sy","--yanzheng_socks5",action="store_true",dest="yanzheng_socks5",
                      help="验证socks5代理池")
    par.add_argument("-sq","--socks5_switch",action="store_true",dest="socks5_switch",
                      help="切换socks5代理池")
    par.add_argument("-v","--version",action="store_true",dest="version",
                      help="获取当前版本")
    par.add_argument("---------------------","------------------------------------",action="store_true",dest="",
                      help="")
    par.add_argument("-R","--re_time",type=str,dest="time",
                     help="更换ip切换速率,0.2等于0.2秒")
    par.add_argument("-P","--re_prot",type=str,dest="prot",
                     help="更换端口号,(默认:33333)")
    par.add_argument("-Qc","--qu_chong",type=str,dest="qu_chong",
                     help="后面跟上要去重的ip池路径文件")
    par.add_argument("-Sz","--switch_zz",type=str,dest="switch_zz",
                     help="切换代理,但不使用全局代理,支持Linux(默认端口33333),参数:http 和 socks5")
    par.add_argument("-Cy","--chi_xu_yz",type=str,dest="chi_xu_yz",
                     help="验证http代理,后面跟上http代理文件路径即可")
    par.add_argument("-K","--Key_mac",type=str,dest="key_mac",
                     help="后面输入自己的key,进行初始化")
    par.add_argument("----------------------","-------------------------------------",action="store_true",dest="",
                      help="")

    args = par.parse_args()

    if args.fofa_get_ip:
        a = get_http_0.main()
    elif args.key_mac:
        print(args.key_mac)
        a = config.config.key_initialize(args.key_mac)
        get_http_0.main()
        print(a)
    elif args.ver_out_ip:
        print('-----------------------------------')
        print('---   开始验证ip,CTRL+C停止     ---')
        print('-----------------------------------')
        http_yanzheng.main()

    elif args.switch_ip:
        # print('开始切换ip,CTRL+C停止')
        print('-----------------------------------')
        print('---   开始切换ip,CTRL+C停止     ---')
        print('-----------------------------------')
        proxy_qh.main()
    elif args.automatic_ip:
        # print('--- 全自动模式 ---')
        print('-----------------------------------')
        print('---        全自动模式          ---')
        print('-----------------------------------')
        file_path = f"output/proxy.txt"
        with open(file_path, "w") as file:
            pass
        a = get_http_0.main()
        http_yanzheng.main()
        print('------------------------\n  开始切换ip地址(默认0.2秒)  \n------------------------')
        proxy_qh.main()
    elif args.time:
        config.config.ip_sulv(args.time)
        print('你调整的速率为:',args.time)
    elif args.prot:
        config.config.prot_sulv(args.prot)
        print('端口号调整为:',args.prot)
    elif args.version:
        print('------------------------------------------------------------')
        print('---                  软件名称: Yccol-Pro                 ---')
        print(f'---                   当前版本: {config.config.version}                   ---')
        print('--- 如需源码或定制,请联系QQ: 323002946 或微信: Yancy_76  ---')
        print('------------------------------------------------------------')
    elif args.get_socks5:
        file_path = f"output/socks5_v.txt"
        with open(file_path, "w") as file:
            pass
        html = get_socks5_0.main()

    elif args.yanzheng_socks5:
        print('-----------------------------------')
        print('---       socks5代理验证中       ---')
        print('-----------------------------------')
        # html = socks5_yanzheng.socks5_yz()
        html = socks5_yanzheng.socks5_yz()
    elif args.socks5_switch:
        print('-----------------------------------')
        print('---       socks5代理切换中       ---')
        print('-----------------------------------')
        html = proxy_qh_sk5.main()
    elif args.qu_chong:
        print('-----------------------------------')
        print('---       ip池去重中.....       ---')
        print('-----------------------------------')
        html = data_process.process_output.qu_chong(args.qu_chong)
    elif args.switch_zz:
        if args.switch_zz == 'http':

            try:
                http_yanzheng.main()
                time.sleep(10)
                asyncio.run(proxy_zz_http.main())
            except KeyboardInterrupt:
                asyncio.run(proxy_zz_http.disable_proxy())
                print("程序已手动停止。")
        elif args.switch_zz == 'socks5':
            a = """
        ------------------
        # 暂不支持socks5 #
        ------------------
        """
            print(a)
        else :
            print('嘿,输入的参数不支持')

    elif args.chi_xu_yz:
        try:
            asyncio.run(for_yan_zheng_http.verify_proxies_file(args.chi_xu_yz))
        except KeyboardInterrupt:
            print("程序已手动停止。")


    else:
        # a = """
        # 杨CC-当前版本:V1.0
        # """

        print('请输入: Yccol-Pro.exe -h 获取帮助')



if __name__ == "__main__":
    print('------------------------------------------------------------')
    print('---                  软件名称: Yccol-Pro                 ---')
    print(f'---                   当前版本: {config.config.version}                   ---')
    print('--- 如需源码或定制,请联系QQ: 323002946 或微信: Yancy_76  ---')
    print('------------------------------------------------------------\n')
    main()