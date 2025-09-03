from flask import Flask, jsonify, request
import mysql.connector
from datetime import datetime
from request_abt import get_request,accuracy_X,di_qu
from data_process import http_yanzheng,https_yanzheng
import IP_address
# from config import config
# from getmac import get_mac_address

app = Flask(__name__)

# 确保返回的 JSON 内容不进行 ASCII 编码
app.json.ensure_ascii = False

def get_db_connection():
    connection = mysql.connector.connect(
        host='49.232.127.250',      # 数据库主机地址
        user='Yccol_API',  # 数据库用户名
        password='jDfJEScxx2rE6CmF',  # 数据库密码
        database='Yccol_API',  # 数据库名称
        connect_timeout=300
    )
    return connection

# 验证获取信息
@app.route('/api/users', methods=['GET'])
def get_users():
    key = request.args.get('key')  # 获取 key 参数
    proxy = request.args.get('proxy')
    # quantity = request.args.get('quantity')
    area = request.args.get('area') #地区
    quantity = request.args.get('quantity') #数量
    accuracy = request.args.get('accuracy') #获取数量
    # 如果没有提供 key 参数，返回错误
    if not key or not proxy or not area:
        return jsonify({"error": "缺少必要参数",
                        "key":"提供的秘钥",
                        "proxy":"需要的代理,支持http & https和socks5",
                        "area":"地区:当前仅支持:all(全部),cn(中国),fcn(国外)指定地区当前只支持http & https,不支持socks5,其他国家暂不支持指定",
                        "accuracy":"(非必要参数)代理验证次数(默认为1),可选参数1(代理一次验证),参数2:(代理验证两次),参数3:代理验证3次(一分钟更新一次)",
                        "quantity":"获取数量,不可以与accuracy一起使用,会有一个没有效果"}), 400

    # 链接数据库
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    # 查询数据库是否存在该key
    cursor.execute("SELECT * FROM Yccol_API WHERE `key` = %s", (key,))
    result = cursor.fetchone()

    # 如果key不存在
    if not result:
        cursor.close()
        connection.close()
        return jsonify({"error": "秘钥错误，请联系开发者购买秘钥"}), 403

    # 验证当前时间是否大于 end_time
    current_time = datetime.now()
    end_time = result['end_time']

    # 如果当前时间大于 end_time，返回过期信息
    if current_time > end_time:
        cursor.close()
        connection.close()
        return jsonify({"error": "秘钥已经过期，请续费或购买新的秘钥"}), 403

    # 如果秘钥有效，返回数据
    if proxy == 'http':
        if area == 'all':
            if accuracy == '1':
                yanzhengcishu,proxies,line_count = accuracy_X.accuracy_1()
            elif accuracy == '2':
                yanzhengcishu,proxies,line_count = accuracy_X.accuracy_2()
            elif accuracy == '3':
                yanzhengcishu,proxies,line_count = accuracy_X.accuracy_3()
            else :
                if quantity is None:
                    yanzhengcishu,proxies,line_count = accuracy_X.accuracy_4()
                else:
                    yanzhengcishu,proxies,line_count = accuracy_X.accuracy_4()
                    # print(quantity)
                    proxies,line_count = accuracy_X.shuliang_mokuai(quantity,proxies,line_count)
        ####################################################
        # 中国区域的选择
        ####################################################
        elif area == 'cn':
            a = 'output/diqu/cn_http_90+.txt'
            b = 'output/diqu/cn.txt'
            if accuracy == '1' or accuracy == '2' or accuracy == '3':
                if quantity is None:
                    yanzhengcishu,proxies,line_count = di_qu.accuracy_4(a)
                else:
                    yanzhengcishu,proxies,line_count = di_qu.accuracy_4(a)
                    # print(quantity)
                    proxies,line_count = di_qu.shuliang_mokuai(quantity,proxies,line_count)
            else :
                if quantity is None:
                    yanzhengcishu,proxies,line_count = di_qu.accuracy_4(b)
                else:
                    yanzhengcishu,proxies,line_count = di_qu.accuracy_4(b)
                    # print(quantity)
                    proxies,line_count = di_qu.shuliang_mokuai(quantity,proxies,line_count)
        elif area == 'fcn':
            a = 'output/diqu/fcn_http_90+.txt'
            b = 'output/diqu/fcn.txt'
            if accuracy == '1' or accuracy == '2' or accuracy == '3':
                if quantity is None:
                    yanzhengcishu,proxies,line_count = di_qu.accuracy_4(a)
                else:
                    yanzhengcishu,proxies,line_count = di_qu.accuracy_4(a)
                    # print(quantity)
                    proxies,line_count = di_qu.shuliang_mokuai(quantity,proxies,line_count)
            else :
                if quantity is None:
                    yanzhengcishu,proxies,line_count = di_qu.accuracy_4(b)
                else:
                    yanzhengcishu,proxies,line_count = di_qu.accuracy_4(b)
                    # print(quantity)
                    proxies,line_count = di_qu.shuliang_mokuai(quantity,proxies,line_count)
    elif proxy == 'https':
        if area == 'all':
            if accuracy == '1':
                yanzhengcishu,proxies,line_count = accuracy_X.accuracy_1()
            elif accuracy == '2':
                yanzhengcishu,proxies,line_count = accuracy_X.accuracy_2()
            elif accuracy == '3':
                yanzhengcishu,proxies,line_count = accuracy_X.accuracy_3()
            else :
                if quantity is None:
                    yanzhengcishu,proxies,line_count = accuracy_X.accuracy_4()
                else:
                    yanzhengcishu,proxies,line_count = accuracy_X.accuracy_4()
                    # print(quantity)
                    proxies,line_count = accuracy_X.shuliang_mokuai(quantity,proxies,line_count)
        ####################################################
        # 中国区域的选择
        ####################################################
        elif area == 'cn':
            a = 'output/diqu/cn_https_90+.txt'
            b = 'output/diqu/cn_https_90-.txt'
            if accuracy == '1' or accuracy == '2' or accuracy == '3':
                if quantity is None:
                    yanzhengcishu,proxies,line_count = di_qu.accuracy_4(a)
                else:
                    yanzhengcishu,proxies,line_count = di_qu.accuracy_4(a)
                    # print(quantity)
                    proxies,line_count = di_qu.shuliang_mokuai(quantity,proxies,line_count)
            else :
                if quantity is None:
                    yanzhengcishu,proxies,line_count = di_qu.accuracy_4(b)
                else:
                    yanzhengcishu,proxies,line_count = di_qu.accuracy_4(b)
                    # print(quantity)
                    proxies,line_count = di_qu.shuliang_mokuai(quantity,proxies,line_count)

        elif area == 'fcn':
            a = 'output/diqu/fcn_https_90+.txt'
            b = 'output/diqu/fcn_https_90-.txt'
            if accuracy == '1' or accuracy == '2' or accuracy == '3':
                if quantity is None:
                    yanzhengcishu,proxies,line_count = di_qu.accuracy_4(a)
                else:
                    yanzhengcishu,proxies,line_count = di_qu.accuracy_4(a)
                    # print(quantity)
                    proxies,line_count = di_qu.shuliang_mokuai(quantity,proxies,line_count)
            else :
                if quantity is None:
                    yanzhengcishu,proxies,line_count = di_qu.accuracy_4(b)
                else:
                    yanzhengcishu,proxies,line_count = di_qu.accuracy_4(b)
                    # print(quantity)
                    proxies,line_count = di_qu.shuliang_mokuai(quantity,proxies,line_count)
    elif proxy == 'socks5':
        if area == 'all':
            if accuracy == '1':
                yanzhengcishu,proxies,line_count = accuracy_X.accuracy_1_socks5()
            elif accuracy == '2':
                yanzhengcishu,proxies,line_count = accuracy_X.accuracy_2_socks5()
            elif accuracy == '3':
                yanzhengcishu,proxies,line_count = accuracy_X.accuracy_3_socks5()
                
            else :
                # yanzhengcishu,proxies,line_count = accuracy_X.accuracy_4_socks5()
                if quantity is None:
                    yanzhengcishu,proxies,line_count = accuracy_X.accuracy_4_socks5()
                else:
                    proxies,line_count = accuracy_X.shuliang_mokuai(quantity,proxies,line_count)

    cursor.close()
    connection.close()

    return jsonify({
        "message": "秘钥有效，数据返回成功",
        "version":"V 0.3",
        "data": result,
        "proxies": proxies,
        "代理个数": line_count,
        "验证次数": yanzhengcishu,
        "代理类型": proxy,
        "地区":area,
        "end_time" : end_time.strftime('%Y-%m-%d %H:%M:%S')
    })


def clean_mac(mac: str) -> str:
    """清洗MAC地址格式（小写无分隔符）"""
    return mac.lower().replace(':', '').replace('-', '') if mac else ''
    return mac

# 验证获取信息
@app.route('/api/key', methods=['GET'])
def get_key():
    key = request.args.get('key')
    input_mac = request.args.get('mac_id')
    proxy = request.args.get('proxy')
    area = request.args.get('area') #地区
    quantity = request.args.get('quantity') #数量
    accuracy = request.args.get('accuracy') #获取数量
    if not key or not input_mac:
        return jsonify({"error": "缺少必要参数", "required_params": ["key", "mac_id"]}), 400

    cleaned_mac = clean_mac(input_mac)
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        # 第一次查询：检查密钥是否存在
        cursor.execute("SELECT * FROM Yccol_API WHERE `key` = %s", (key,))
        key_data = cursor.fetchone()
        if not key_data:
            return jsonify({"error": "无效密钥"}), 403

        # 检查密钥有效期
        current_time = datetime.now()
        end_time = key_data['end_time']
        if current_time > end_time:
            return jsonify({"error": "密钥已过期"}), 403

        stored_mac = clean_mac(key_data.get('mac_id', ''))

        # 首次绑定 MAC 地址
        if not stored_mac:
            # 执行 UPDATE
            cursor.execute(
                "UPDATE Yccol_API SET mac_id = %s WHERE `key` = %s",
                (cleaned_mac, key)
            )
            connection.commit()

            # 重新查询以获取更新后的数据
            cursor.execute("SELECT * FROM Yccol_API WHERE `key` = %s", (key,))
            updated_data = cursor.fetchone()
            # 如果秘钥有效，返回数据
        if proxy == 'http':
            if area == 'all':
                if accuracy == '1':
                    yanzhengcishu,proxies,line_count = accuracy_X.accuracy_1()
                elif accuracy == '2':
                    yanzhengcishu,proxies,line_count = accuracy_X.accuracy_2()
                elif accuracy == '3':
                    yanzhengcishu,proxies,line_count = accuracy_X.accuracy_3()
                else :
                    if quantity is None:
                        yanzhengcishu,proxies,line_count = accuracy_X.accuracy_4()
                    else:
                        yanzhengcishu,proxies,line_count = accuracy_X.accuracy_4()
                        # print(quantity)
                        proxies,line_count = accuracy_X.shuliang_mokuai(quantity,proxies,line_count)
                        


        elif proxy == 'socks5':
            if area == 'all':
                if accuracy == '1':
                    yanzhengcishu,proxies,line_count = accuracy_X.accuracy_1_socks5()
                elif accuracy == '2':
                    yanzhengcishu,proxies,line_count = accuracy_X.accuracy_2_socks5()
                elif accuracy == '3':
                    yanzhengcishu,proxies,line_count = accuracy_X.accuracy_3_socks5()
                    
                else :
                    yanzhengcishu,proxies,line_count = accuracy_X.accuracy_4_socks5()
                    if quantity is None:
                        yanzhengcishu,proxies,line_count = accuracy_X.accuracy_4_socks5()
                    else:
                        proxies,line_count = accuracy_X.shuliang_mokuai(quantity,proxies,line_count)
        else : 
            print() 
            return jsonify({
                "message": "秘钥有效，数据返回成功",
                "version": "V 0.3",
                "data": {
                    "create_time": updated_data['create_time'],
                    "end_time": updated_data['end_time'],
                    "id": updated_data['id'],
                    "key": updated_data['key'],
                    "mac_id": updated_data['mac_id'],  # 确保使用更新后的值
                    "备注": updated_data.get('备注', '')

                },
                "proxies": proxies,
                "代理个数": line_count,
                "验证次数": yanzhengcishu,
                "代理类型": proxy,
                # "end_time" : end_time.strftime('%Y-%m-%d %H:%M:%S')
                "end_time": updated_data['end_time'].strftime('%Y-%m-%d %H:%M:%S')
            })

        # MAC 地址验证
        if stored_mac != cleaned_mac:
            return jsonify({"error": "设备未授权"}), 403
        
        # 返回最新数据
        return jsonify({
            "message": "秘钥有效，数据返回成功",
            "version": "V 0.3",
            "data": {
                "create_time": key_data['create_time'],
                "end_time": key_data['end_time'],
                "id": key_data['id'],
                "key": key_data['key'],
                "mac_id": key_data['mac_id'],
                "备注": key_data.get('备注', ''),
                # "代理数量":""
            },
            "proxies": proxies,
            "代理个数": line_count,
            "验证次数": yanzhengcishu,
            "代理类型": proxy,
            "end_time": end_time.strftime('%Y-%m-%d %H:%M:%S')
        })

    except mysql.connector.Error as e:
        connection.rollback()
        return jsonify({"error": f"数据库错误: {str(e)}"}), 500
    finally:
        cursor.close()
        connection.close()


@app.route('/api/v2/http', methods=['GET'])
def get_500_http():
        yanzhengcishu,proxies,line_count = accuracy_X.http_500()
        return jsonify({
        "version":"V 0.3",
        "proxies": proxies,
        "代理个数": line_count,
        "验证次数": yanzhengcishu,
        "代理类型": 'http',

    })

@app.route('/api/v2/socks5', methods=['GET'])
def get_500_socks5():
        
        yanzhengcishu,proxies,line_count = accuracy_X.socks5_500()
        return jsonify({
        "version":"V 0.3",
        "proxies": proxies,
        "代理个数": line_count,
        "验证次数": yanzhengcishu,
        "代理类型": 'http',
    })


@app.route('/api/v1/ip_dingwei',methods=['GET'])
def ip_ding_wei():
        from config import ip_dingwei
        ip = request.args.get('ip')
        a,b,c,d,e,f,g = ip_dingwei.main(ip)
        return jsonify({
        "version":"V 0.3",
        "Help":"帮助信息:此IP定位使用的IP2Location库,而且此定位为临时免费,后续逐步精准度会上升,最终目标位:10米以内",
        
        "国家": a,
        "地区": b,
        "城市": c,
        "经度": d,
        "纬度": e,
        "邮编": f,
        "时区": g,
        "如何定位:":"访问:https://lbs.amap.com/tools/picker 输入经纬度即可"

    })


if __name__ == '__main__':
    # 启动调度器
    IP_address.start_scheduler()
    app.run(host='0.0.0.0',port=3751)
