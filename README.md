# Yccol - 基于FOFA抓取的代理池工具

![版本](https://img.shields.io/badge/版本-V1.1-blue)
![语言](https://img.shields.io/badge/语言-Python-green)
![协议](https://img.shields.io/badge/协议-HTTP/HTTPS/SOCKS5-orange)

Yccol 是一个基于 FOFA 搜索引擎抓取的代理池工具，提供多种版本以满足不同用户需求。该系统能够自动获取、验证和管理代理 IP，支持 HTTP、HTTPS 和 SOCKS5 等多种代理协议，并提供 API 接口、命令行工具和图形界面等多种使用方式。

查看框架请查看 [arch.md]()

## 项目版本

本项目包含多个版本，满足不同场景的需求：

- **API 版本**：提供 RESTful API 接口，支持远程调用
- **Pro 版本**：高级命令行工具，提供完整功能
- **GUI 版本**：图形用户界面，易于操作
- **基础版本(fifa0)**：简化版命令行工具，提供核心功能

## 功能特点

- 基于 FOFA 搜索引擎抓取代理 IP
- 多线程验证代理可用性
- 支持 HTTP、HTTPS 和 SOCKS5 代理
- 提供 API 接口供第三方调用
- 支持代理 IP 自动切换
- 支持按地区筛选代理 IP
- 提供命令行和图形界面操作

## 环境要求

- Python 3.6+
- 网络连接（访问 FOFA 搜索引擎）
- FOFA API 密钥
- 系统管理员权限（用于设置系统代理）

### 依赖库

```
flask
mysql-connector-python
requests
PyQt5 (仅GUI版本需要)
```

## 安装与配置

### 1. 克隆项目

```bash
git clone https://github.com/SGYLING/yccol.git
cd yccol
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 配置 FOFA API 密钥

在 `config/conf.txt` 文件中添加您的 FOFA API 密钥：

```
fofa_key='your_fofa_api_key'
```

> 注意：只要注册登录 FOFA 就有免费的 API 密钥，不需要会员也可以使用（功能会受限）。

## 使用说明

### API 版本使用

API 版本提供 RESTful 接口，允许用户通过 HTTP 请求获取和管理代理 IP。

#### 启动 API 服务

```bash
cd API
python app.py
```

#### API 接口说明

- **获取代理 IP**：`/api/users`
  - 参数：
    - `key`：API 密钥（必填）
    - `proxy`：代理类型，支持 http、https、socks5（必填）
    - `area`：地区，支持 all（全部）、cn（中国）、fcn（国外）（必填）
    - `accuracy`：代理验证次数，可选 1-3（非必填，默认为 1）
    - `quantity`：获取数量（非必填，不可与 accuracy 同时使用）

#### 示例请求

```
http://localhost:5000/api/users?key=your_api_key&proxy=http&area=cn
```

### Pro 版本使用

Pro 版本是一个功能完整的命令行工具，提供更多高级功能和选项。

#### 命令行参数

```bash
cd Pro
python Yccol-Pro.py [参数]
```

#### 参数说明

| 参数 | 全称 | 说明 |
|------|------|------|
| -f | --fofa_get_ip | 通过 FOFA 获取 IP |
| -vo | --Ver_out_ip | 验证 IP |
| -s | --switch_ip | 开启切换 IP 功能 |
| -a | --Automatic_ip | 自动运行整套程序 |
| -fs | --get_socks5 | 获取 SOCKS5 代理池 |
| -sy | --yanzheng_socks5 | 验证 SOCKS5 代理池 |
| -sq | --socks5_switch | 切换 SOCKS5 代理池 |
| -v | --version | 获取当前版本 |
| -R | --re_time | 更换 IP 切换速率，如 0.2 秒 |
| -P | --re_prot | 更换端口号（默认：33333） |
| -Qc | --qu_chong | 去重 IP 池文件 |
| -Sz | --switch_zz | 切换代理但不使用全局代理，支持 Linux |
| -Cy | --chi_xu_yz | 验证 HTTP 代理 |
| -K | --Key_mac | 初始化密钥 |

#### 示例命令

```bash
# 获取代理 IP
python Yccol-Pro.py -f

# 验证代理 IP
python Yccol-Pro.py -vo

# 自动运行整套程序
python Yccol-Pro.py -a

# 设置 IP 切换速率为 0.5 秒
python Yccol-Pro.py -R 0.5
```

### GUI 版本使用

GUI 版本提供图形用户界面，方便非技术用户使用。

#### 启动 GUI

```bash
cd GUI
python "Yccol - GUI.py"
```

#### 使用步骤

1. 输入密钥进行验证
2. 在主界面选择需要的功能：
   - 获取代理
   - 验证代理
   - 切换代理
   - 设置参数

### 基础版本使用

基础版本是一个简化的命令行工具，提供核心功能。

#### 启动基础版本

```bash
cd fifa0
python fifa0.py
```

#### 使用步骤

运行后会显示菜单，输入对应数字选择功能：
1. 获取代理
2. 验证代理
3. 开启代理切换
4. 全自动操作（包含：获取代理、验证代理、代理切换）

## 配置文件说明

### config/conf.txt

主要配置文件，包含以下设置：

```
fofa_key='your_fofa_api_key'  # FOFA API 密钥
get_time='0.2'  # IP 切换速率，单位为秒
port='33333'  # 代理端口号
```

### config/config.py

包含更多高级配置，如：

- FOFA 查询语句（Base64 编码）
- 不同地区的查询参数
- 版本信息
- 配置文件处理函数

## 数据文件

### output/proxy.txt

存储获取到的 HTTP/HTTPS 代理 IP

### output/proxy_v.txt

存储验证后的可用 HTTP/HTTPS 代理 IP

### output/socks5.txt

存储获取到的 SOCKS5 代理 IP

### output/socks5_v.txt

存储验证后的可用 SOCKS5 代理 IP

## 工作流程

1. **获取代理**：从 FOFA 搜索引擎获取代理 IP
2. **验证代理**：多线程验证代理 IP 的可用性
3. **管理代理**：将可用代理保存到文件
4. **切换代理**：根据配置的速率自动切换代理 IP

## 注意事项

1. 使用前请确保已配置有效的 FOFA API 密钥
2. 切换代理功能需要管理员权限
3. 代理池的质量取决于 FOFA 搜索结果
4. 建议定期更新代理池以保证可用性
5. 使用 API 版本需要配置 MySQL 数据库

## 常见问题

### 无法获取代理 IP

- 检查 FOFA API 密钥是否正确
- 检查网络连接是否正常
- 检查 FOFA API 调用次数是否超限

### 代理验证失败率高

- 代理 IP 本身可能不稳定
- 尝试增加验证超时时间
- 尝试使用不同地区的代理

### 代理切换不生效

- 确保以管理员权限运行
- 检查端口是否被占用
- 检查系统代理设置是否正确

## 联系方式

- B站UP主：疯狂的杨CC
- QQ：323002946
- 微信：Yancy_76

## 版本信息

当前版本：V1.1

## 许可证

本项目采用 MIT 许可证。详见 LICENSE 文件。

## 致谢

感谢 FOFA 搜索引擎提供的数据支持。