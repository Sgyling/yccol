from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
import atexit
from request_abt import get_request,accuracy_X
from config import YZ_di_qu_http, config
from data_process import http_yanzheng,socks5_yanzheng,get_500

app = Flask(__name__)
"""
################################################################################
http 代理任务模块
################################################################################
"""
# 定义要定时执行的路由函数
@app.route('/ten_minutes_task')
def ten_minutes_task():

    # # 先清空一下本来的数据
    # file_path = f"output/proxy.txt"
    # with open(file_path, "w") as file:
    #     pass
    get_request.get_http(config.get_http_url)
    http_yanzheng.main()
    YZ_di_qu_http.main()
    # print("每 120 分钟获取一次http代理并验证   成功")
    return "任务已运行"

# 定义定时任务函数
def run_ten_minutes_task():
    with app.app_context():
        # 调用路由函数
        ten_minutes_task()

# 定义二次验证时间
def ten_minutes_task2():
    

    # 先清空一下本来的数据
    file_path = f"output/http2.txt"
    with open(file_path, "w") as file:
        pass
    # get_request.get_http(config.get_http_url)
    http_yanzheng.main2()
    print("每 10 分钟进行一次二次代理验证    成功")
    return "任务已运行"

# 定义定时任务函数2
def run_ten_minutes_task2():
    with app.app_context():
        # 调用路由函数
        ten_minutes_task2()

# 定义二次验证时间
def ten_minutes_task3():
    
    # 先清空一下本来的数据
    file_path = f"output/http3.txt"
    with open(file_path, "w") as file:
        pass
    # get_request.get_http(config.get_http_url)
    http_yanzheng.main3()
    print("每 2 分钟进行一次三次代理验证     成功")
    return "任务已运行"

# 定义定时任务函数3
def run_ten_minutes_task3():
    with app.app_context():
        # 调用路由函数
        ten_minutes_task3()
"""
################################################################################
socks5 代理任务模块
################################################################################
"""
# 获取socks5,定时任务
def ten_socks5():
    # print("每 120 分钟获取一次socks5代理,并进行一次验证")

    # 先清空一下本来的数据
    file_path = f"output/socks5_v.txt"
    with open(file_path, "w") as file:
        pass
    html = get_request.get_socks5()
    html2 = socks5_yanzheng.socks5_yz()
    print("每 120 分钟获取一次socks5代理,并进行一次验证. 成功")
    return "任务已运行"

# 定义定时任务函数
def run_ten_socks5():
    with app.app_context():
        # 调用路由函数
        ten_socks5()

# 二次验证socks5

def ten_socks5_2():
    socks5_yanzheng.socks5_yz_2()
    print("第二次验证socks5 成功")
    return "任务已运行"

# 定义定时任务函数
def run_ten_socks5_2():
    with app.app_context():
        # 调用路由函数
        ten_socks5_2()

# 三次验证socks5
def ten_socks5_3():
    socks5_yanzheng.socks5_yz_3()
    print("第三次验证socks5. 成功")
    return "任务已运行"

# 定义定时任务函数
def run_ten_socks5_3():
    with app.app_context():
        # 调用路由函数
        ten_socks5_3()

"""
################################################################################
免费获取500个http代理模块
################################################################################
"""

# 免费500模块
def get_http_500():
    # socks5_yanzheng.socks5_yz_3()
    # accuracy_X.http_500()
    get_500.http_500()
    # print("第三次验证socks5. 成功")
    return "500已验证"

# 定义定时任务函数
def run_get_http_500():
    with app.app_context():
        # 调用路由函数
        # ten_socks5_3()
        get_http_500()


# 免费500模块
def get_socks5_500():
    # socks5_yanzheng.socks5_yz_3()
    # accuracy_X.http_500()
    get_500.socks5_500()
    # print("第三次验证socks5. 成功")
    return "500已验证"

# 定义定时任务函数
def run_get_socks5_500():
    with app.app_context():
        # 调用路由函数
        # ten_socks5_3()
        get_socks5_500()

"""
################################################################################
验证地区所属国家的模块
################################################################################
"""
# 验证地区所属国家的模块
def get_di_qu_yanzheng():
    YZ_di_qu_http.main()
    return "已验证"

# 验证地区所属国家的模块
def run_get_di_qu_yanzheng():
    with app.app_context():
        # 调用路由函数
        # ten_socks5_3()
        get_di_qu_yanzheng()

"""
################################################################################
验证中国的代理池ip的定时模块
################################################################################
"""
# 验证地区所属国家的模块
def get_cn_yanzheng():
    http_yanzheng.main_cn()
    return "验证中国地区的代理池完成"

# 验证地区所属国家的模块
def run_get_cn_yanzheng():
    with app.app_context():
        get_cn_yanzheng()



"""
################################################################################
定时任务模块
################################################################################
"""

# 创建调度器
scheduler = BackgroundScheduler()
# 120分钟获取一次http和socks5代理池,并进行一次验证
scheduler.add_job(func=run_ten_minutes_task, trigger='interval', minutes=120)

# 180 分钟获取一次socks5代理
scheduler.add_job(func=run_ten_socks5, trigger='interval', minutes=120)

# 120分钟筛选一次免费版本的代理池
scheduler.add_job(func=run_get_http_500, trigger='interval', minutes=120)
scheduler.add_job(func=run_get_socks5_500, trigger='interval', minutes=120)

# 20分钟进行二次验证http代理池
scheduler.add_job(func=run_ten_minutes_task2, trigger='interval', minutes=10)

# 60分钟进行socks5代理池的二次验证
scheduler.add_job(func=run_ten_socks5_2, trigger='interval', minutes=60)

# 5 分钟验证一次ip地区
# scheduler.add_job(func=run_get_di_qu_yanzheng, trigger='interval', minutes=1)
# 3分钟验证一次中国的ip池
# scheduler.add_job(func=run_get_cn_yanzheng, trigger='interval', minutes=3)


# 每分钟进行三次验证http和socks5代理池
scheduler.add_job(func=run_ten_minutes_task3, trigger='interval', minutes=2)

scheduler.add_job(func=run_ten_socks5_3, trigger='interval', minutes=30)

# 启动调度器
def start_scheduler():
    scheduler.start()
    # 在应用退出时关闭调度器
    atexit.register(lambda: scheduler.shutdown())