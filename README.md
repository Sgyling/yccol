---
title: Yccol-全自动代理池更换工具
date: 2025-02-24 15:46:40
tags: 代理池
categories: 渗透
---

Yccol：https://pan.quark.cn/s/3ab113051416

Yccol-GUI连接:https://pan.quark.cn/s/283ac2d54a3e

github:https://github.com/Sgyling/yccol

带图介绍连接:https://yancy77.cn

2.22号 Fifa0更名为:Yccol

Yccol更新预告

| 版本      | 支持http | 支持socks4 | 支持socks5 | 本次更新内容 |
| --------- | -------- | ---------- | ---------- | ------------ |
| Yccol     | √        | ×          | √          | socks5验证   |
| Yccol-Pro | √        | ×          | √          | socks5切换   |
| Yccol-API | √        | ×          | ×          | 内测上线     |
| Yccol-GUi | √        | ×          | ×          | 内测上线     |



# 更新内容

## 2.24号Yccol-Pro更新 V1.1.2版本

- [添加] - 添加了-sq 参数,功能为:socks5的代理池切换功能
- [优化] - 优化了输出外观
- [优化] - 优化了抓取ip的 速度
- [更新] - 在不使用参数的情况下,自动输出提示和获取http代理
- [更新] - 在使用-f 或 没有任何参数时,锁定100个IP源

![](https://pic1.imgdb.cn/item/67bc1fbbd0e0a243d4034abf.png)

---

## 2.24号Yccol更新 V1.1.1 版本

- 添加了socks5的代理验证功能.
- 固定了socks5代理获取的数量,固定100
- 修复了部分bug

![](https://pic1.imgdb.cn/item/67bc23ffd0e0a243d403501e.png)

---



## 2.23号 Yccol-GUI内测上线

Yccol-GUI是一款获取代理池工具的软件,而且支持验证代理的工具

先看截图:

![](https://pic1.imgdb.cn/item/67bb09fed0e0a243d4029940.png)

这里输入秘钥,临时秘钥ccc后,点击检测秘钥

----

![](https://pic1.imgdb.cn/item/67bb0a47d0e0a243d40299a5.png)

进入后界面如下(目前只开放http)

---

直接点击获取ip池,可能需要卡顿一会,这是在获取代理池,

![](https://pic1.imgdb.cn/item/67bb0aafd0e0a243d40299be.png)



----

获取代理后,点击验证ip池,就可以把可用的代理筛选出来

![](https://pic1.imgdb.cn/item/67bb0afbd0e0a243d4029a38.png)

如果想要多筛选两次,那就多点两次验证ip池

----

怎么批量验证自己的ip地址呢?

![](https://pic1.imgdb.cn/item/67bb0b48d0e0a243d4029a60.png)

将自己的ip粘贴到文本框中,即可验证(目前仅支持http代理)

----

其他功能

![](https://pic1.imgdb.cn/item/67bb0b88d0e0a243d4029a7b.png)

---





## 2.22号 Yccol更名为:Yccol

## - Yccol-API内测上线

```
请求:GET
API连接:http://api.Yccol.cc:3751/api/users
参数:key,proxy,area,accuracy
参数介绍:
	key(必要的):后面需要跟着自己的秘钥
	proxy(必要的):当前仅支持http,暂不支持:socks5
	area(必要的):当前仅支持:all参数,不支持指定地区
	accuracy(非必要的):支持:1\2\3三个阶段的筛选,(3为精准度最高,每分钟抓取一次。2为筛选两次的ip池地址，5-10分钟抓取一次。1为筛选一次，可用率最低，约120分钟抓取一次)

使用介绍：
	http://api.Yccol.cc:3751/api/users?key=XXXXXX&proxy=all&area=all&accuracy=1\2\3(选择一个参数即可)
```



## 2.20号 Yccol-ProV1.1.1 版本

### Yccol-Pro更新内容

- [优化] - 优化了输出过程,使其输出更加美观
- [优化] - 优化了代码逻辑
- [更新] - 更新了 -f ,现在-f 后面可以跟自己所需要的ip源数量了
- [更新] - socks5代理验证功能添加了多线程处理

## 2.19号V1.1版本

### Yccol-更新内容

- [添加] - 添加了对socks5代理支持
- [优化] - 优化了部分显示,让其看起来比较好看
- [优化] - 优化了http代理验证的算法,让http代理延迟更低!也更快!

### Yccol-Pro 更新内容

- [添加] - 添加了对socks5的代理支持

- [添加] - 添加了sosck5代理池的验证功能

- [添加] - 添加了 [-v] 参数,获取当前版本

- [更新] - 参数 -VO 更新为 -vo 参数,

- [更新] - 参数 -A 更新为: -a 参数

- [回退] - 取消了 -VO -V -O 三个参数,用到的不多(依然可以验证ip池)

- [回退] - 取消了 -UP 更新参数,因为最近在部署API的问题,需要经常活动服务器,指不定怎么着就删了

- [优化] - 将http代理获取上限调整到了1000(最终可用大概在1000-5000之间,可能会上下波动)

- [优化] - 将socks5代理获取上限调整到了1000(最终可用大概在400-800之间,可能会上下波动)

- [优化] - 取消掉了一些没用的代码,让应用更加的优美~

  

# :satisfied:Yccol-安装及使用

Yccol更新时间:25年-2月19号

Yccol-Pro更新时间:25年-2月-19号

我们下载以后,双击Yccol运行,即可看到下方的说明以及文件配置用法

![](https://pic1.imgdb.cn/item/67b2a818d0e0a243d40015c4.png)

---

## :question:配置环境

更改config/conf.txt中的数据

![](https://pic1.imgdb.cn/item/67b2a87fd0e0a243d40015f3.png)

----

config/conf.txt中存在两个参数

分别为:key 和get_time两个参数,

key中要填写,fofa的key,

![](https://pic1.imgdb.cn/item/67b2a9fed0e0a243d40016f6.png)

fofa的key,需要复制这里的代理,并且粘贴到key参数中,并且fofa中需要有f点及打开F点权益才可以正常使用

![](https://pic1.imgdb.cn/item/67b2aa70d0e0a243d4001710.png)

---

get_time中需要填写代理的切换时间,0.2则是0.2秒进行切换一次代理.默认为0.2

![](https://pic1.imgdb.cn/item/67b2a8cbd0e0a243d4001682.png)

那么到这里,配置完成

---



## :ice_hockey:获取ip代理

![](https://pic1.imgdb.cn/item/67b2ab02d0e0a243d4001727.png)

---

输入1以后,直接回车即可获取代理,获取代理后,均为未筛选的代理,会存放在output/proxy.txt中

运行以后,会出现以下界面,

![](https://pic1.imgdb.cn/item/67b2aba3d0e0a243d4001745.png)

![](https://pic1.imgdb.cn/item/67b2abb7d0e0a243d400174b.png)

![](https://pic1.imgdb.cn/item/67b2abe2d0e0a243d400174f.png)

![](https://pic1.imgdb.cn/item/67b2ac33d0e0a243d400175c.png)

以上情况均为正常情况.

等待完成即可~完成以后如下图,(如果是双击打开的,则完成后会直接退出)

![](https://pic1.imgdb.cn/item/67b2ad08d0e0a243d4001791.png)

---

## :airplane::验证代理

![](https://pic1.imgdb.cn/item/67b2ad59d0e0a243d40017ad.png)

输入2以后,会将output/proxy.txt中的代理,进行批量验证,最终保存到output/http.txt文件当中.

![](https://pic1.imgdb.cn/item/67b2ada1d0e0a243d40017c5.png)

---

## :factory::验证自己的代理

我们除了可以验证使用1参数生成的代理,也可以用来验证自己的代理池ip,

首先,我们需要打开output,文件夹

![](https://pic1.imgdb.cn/item/67b2adfad0e0a243d40017d0.png)

里面存放了两个文件,分别为proxy.txt和http.txt

我们将自己的代理存放在proxy.txt文件当中,一行一个,如下图所示:

![](https://pic1.imgdb.cn/item/67b2ae35d0e0a243d40017e2.png)

存放完成后,保存,运行Yccol.exe

选择'2'参数,运行即可,最终可以使用的代理池,则会存放在http.txt中.

![](https://pic1.imgdb.cn/item/67b2aeccd0e0a243d4001802.png)

则验证成功

----

## :walking::开始切换ip

![](https://pic1.imgdb.cn/item/67b2af11d0e0a243d400181e.png)

输入'3'即可开始切换代理ip,切换ip速度,取决了config/conf.txt中的get_time参数

![](https://pic1.imgdb.cn/item/67b2af53d0e0a243d4001839.png)

![](https://pic1.imgdb.cn/item/67b2af67d0e0a243d4001845.png)

![](https://pic1.imgdb.cn/item/67b2af9bd0e0a243d4001874.png)

如果需要停止,则使用CTRL+C即可停止

---

## :zap::使用自己的ip池进行切换

我们只需要把自己的ip存放在output.txt中,再运行 参数 '3',即可进行ip切换



# 

# :satisfied::Yccol-Pro

FiFa0-Pro是Fifa0的一个付费版本,可以用户免去配置,以及提供一个永久性的key,让用户体验到高端的且牛逼的一款代理池ip切换工具

Yccol-Pro是在Yccol的基础上,进行了进一步优化,和更多的功能,同时操作方式与Yccol也略有不同



## :satisfied:Yccol-Pro教程

首先从作者这里购买Yccol-Pro版本以后,解压到文件夹,并打开终端,

WIndows11,可以直接在Yccol-Pro版本的目录下右键,从终端打开,

![](https://pic1.imgdb.cn/item/67b2b183d0e0a243d400192b.png)

WIndows10可以在目录框中,输入CMD或powershell,进行打开,

![](https://pic1.imgdb.cn/item/67b2b203d0e0a243d4001954.png)

----

打开终端后:

运行:Yccol-Pro -h

![](https://pic1.imgdb.cn/item/67b2b383d0e0a243d40019a4.png)

即可显示参数

----

从参数中我们可以看到,付费版多出了好些参数,

自动验证ip参数\指定验证ip池参数\获取指定地域的ip信息\更换ip切换速率\单独的验证ip\保存ip池\以及更新等多个参数.

## :1st_place_medal::基本使用方式

```
#运行整套功能,并自动开启ip切换
Yccol-pro -a 

# 获取帮助
Yccol-pro -h

# 获取ip池
Yccol-pro -f

# 验证ip是否能用
Yccol-pro -vo

# 验证自己的ip池是否可用
Yccol-peo -V [自己的ip池txt文件路径] -O [要保存的位置] #注意,此处的-O保存位置,只需要写路径即可,例如/'D:\tools\筛选\'不需要带有文件名称

# 验证ip池,并保存到output目录中的http.txt文件
Yccol-pro -V [ip池txt文件路径]

# 切换ip更换速度
Yccol-pro -R [速度]  #例如:0.2等于0.2秒

#获取不同地区的ip池
Yccol-pro -fi [参数] #目前fi参数支持:US(美国),SG(新加坡),KR(韩国),(HK)香港

#更新软件版本
Yccol-pro -up

#开始切换ip
Yccol-pro -S
```

## :o::常见报错

![](https://pic1.imgdb.cn/item/67b2ba05d0e0a243d4001a8b.png)

网络出现问题了,检查网络后再进行下载.

---

如果QQ\微信有网络,但是浏览器没有网络,请运行

Yccol-pro -S 后再运行 CTRL+C 停止,即可回复网络

---

如果提示:未选择参数,

![](https://pic1.imgdb.cn/item/67b2baded0e0a243d4001aaa.png)

那么请使用Yccol-pro -h 进行参数查看

---

运行之后闪退

请在终端中运行即可.

---

如果还有报错,请及时联系:Yancy_76或者QQ323002946

