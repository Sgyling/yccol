import IP2Location
import os

def locate_ip(ip_address, db_path):
    """
    使用IP2Location数据库查询IP地理位置信息
    
    参数:
    ip_address (str): 要查询的IP地址
    db_path (str): IP2Location BIN数据库文件路径
    
    返回:
    dict: 包含地理信息的字典
    """
    try:
        # 初始化数据库对象
        db = IP2Location.IP2Location()
        
        # 打开数据库文件
        db.open(db_path)
        
        # 执行IP查询
        result = db.get_all(ip_address)
        
        return {
            'country': result.country_long,
            'region': result.region,
            'city': result.city,
            'latitude': result.latitude,
            'longitude': result.longitude,
            'zipcode': result.zipcode,
            'timezone': result.timezone
        }
        
    except Exception as e:
        print(f"发生错误: {str(e)}")
        return None
    finally:
        if 'db' in locals():
            db.close()

def main(ip):
    # 设置数据库路径 (替换为你的实际路径)
    db_filename = "IP2LOCATION-LITE-DB11.BIN"
    db_path = os.path.join(os.path.dirname(__file__), db_filename)
    
    # 获取用户输入
    # ip = input("请输入要查询的IP地址: ").strip()
    
    # 执行查询
    result = locate_ip(ip, db_path)
    a = result['country']
    b = result['region']
    c = result['city']
    d = result['latitude']
    e = result['longitude']
    f = result['zipcode']
    g = result['timezone']
    # 显示结果
    if result:
        print("\n查询结果:")
        print(f"国家: {a}")
        print(f"地区: {b}")
        print(f"城市: {c}")
        print(f"纬度: {d}")
        print(f"经度: {e}")
        print(f"邮编: {f}")
        print(f"时区: {g}")
    else:
        print("无法获取位置信息")
    
    return a,b,c,d,e,f,g

if __name__ == "__main__":
    main()