---
title: Yccol-全自动代理池更换工具
date: 2025-02-24 15:46:40
tags: 代理池
categories: 渗透
---

Yccol官网:https://Yccol.cc   

Yccol成品下载:https://pan.quark.cn/s/16ab575efaf0

其他版本,请联系:微信:Yancy_76,或QQ: 323002946,进行下载

# 更新内容 

最新版本:Yccol-Pro V1.3.1

全部的更新历史:

https://yancy77.cn/2025/03/01/Yccol-%E5%9F%BA%E4%BA%8Efofa%E7%9A%84%E5%85%A8%E8%87%AA%E5%8A%A8%E4%BB%A3%E7%90%86%E6%B1%A0%E5%B7%A5%E5%85%B7/#%E6%9B%B4%E6%96%B0%E5%86%85%E5%AE%B9



# :satisfied:Yccol-安装及使用

# 下载安装以及使用:

```
# 注意:Win下需要先安装git命令
$ git clone https://github.com/Sgyling/yccol
$ python -m pip install -r requirements.txt
$ python Yccol.py # 即可开始运行

## 当然哈,咱也可以下载成品 下载链接: https://pan.quark.cn/s/06e0a22c2189
## 成品使用方式,双击打开即可.
## 用法可以往下看一看
```





或者我们我们下载成品以后,双击Yccol运行,即可看到下方的说明以及文件配置用法

![](https://pic1.imgdb.cn/item/67b2a818d0e0a243d40015c4.png)

---

## :question:配置环境

更改config/conf.txt中的数据

![](https://pic1.imgdb.cn/item/67b2a87fd0e0a243d40015f3.png)

----

config/conf.txt中存在两个参数

分别为local_port=和get_time两个参数,

get_time 为切换时间的参数.

local_port 为端口号

---

get_time中需要填写代理的切换时间,0.2则是0.2秒进行切换一次代理.默认为0.2

![](https://pic1.imgdb.cn/item/67c7dbaad0e0a243d40c41f4.png)

那么到这里,配置完成

---



## :ice_hockey:获取ip代理

![](https://pic1.imgdb.cn/item/67c7dc1ad0e0a243d40c420e.png)

---

输入1以后,直接回车即可获取代理,获取代理后,均为未筛选的代理,会存放在output/proxy.txt中

运行以后,会出现以下界面,

![](https://pic1.imgdb.cn/item/67c7dce6d0e0a243d40c423a.png)

---

输入2以后,会获取socks5代理

![获取sosks5](https://pic1.imgdb.cn/item/67c7dc78d0e0a243d40c421e.png)

---

## :airplane::验证代理

![](https://pic1.imgdb.cn/item/67c7dc1ad0e0a243d40c420e.png)

输入3以后,会将output/proxy.txt中的代理,进行批量验证,最终保存到output/http.txt文件当中.

![](https://pic1.imgdb.cn/item/67c7dd2bd0e0a243d40c4244.png)

---

## :factory::验证自己的代理

我们除了可以验证使用1参数生成的代理,也可以用来验证自己的代理池ip,

首先,我们需要打开output,文件夹

![](https://pic1.imgdb.cn/item/67b2adfad0e0a243d40017d0.png)

里面存放了两个文件,分别为proxy.txt和http.txt

我们将自己的代理存放在proxy.txt文件当中,一行一个,如下图所示:

![](https://pic1.imgdb.cn/item/67b2ae35d0e0a243d40017e2.png)

存放完成后,保存,运行Yccol.exe

选择'3'参数,运行即可,最终可以使用的代理池,则会存放在http.txt中.

![](https://pic1.imgdb.cn/item/67b2aeccd0e0a243d4001802.png)

则验证成功

----

## :walking::开始切换ip

![](https://pic1.imgdb.cn/item/67c7dc1ad0e0a243d40c420e.png)

输入'4'即可开始切换代理ip,切换ip速度,取决了config/conf.txt中的get_time参数

![](https://pic1.imgdb.cn/item/67c7dd74d0e0a243d40c4253.png)



如果需要停止,则使用CTRL+C或者直接关闭即可停止

---

## :zap::使用自己的ip池进行切换

我们只需要把自己的ip存放在http.txt中,再运行 参数 '4',即可进行ip切换

# :satisfied::Yccol-Pro

Yccol-Pro是Yccol的一个付费版本,可以用户免去配置,以及提供一个key,让用户体验到高端的且牛逼的一款代理池ip切换工具

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

![](https://pic1.imgdb.cn/item/67c7ddc3d0e0a243d40c425f.png)

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


#更新软件版本
Yccol-pro -up

#开始切换ip
Yccol-pro -S
```

更多参数介绍,请在https://yccol.cc/Yccol-Help.html#pro 中进行查看

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

## 更多错误,请在https://yccol.cc/Yccol-Help.html#pro 中进行查看

---

如果还有报错,请及时联系:Yancy_76或者QQ323002946

