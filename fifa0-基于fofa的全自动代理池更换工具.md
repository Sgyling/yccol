---
title: fifa0-全自动代理池更换工具
date: 2025-02-09 15:46:40
tags: 代理池
categories: 渗透
---

链接：https://pan.quark.cn/s/e88d195e4049

github:https://github.com/Sgyling/fifa0

# :satisfied:FiFa0



我们下载以后,双击fifa0运行,即可看到下方的说明以及文件配置用法

![](https://pic1.imgdb.cn/item/67b2a818d0e0a243d40015c4.png)

---

# :question:配置环境

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



# :ice_hockey:获取ip代理

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

# :airplane::验证代理

![](https://pic1.imgdb.cn/item/67b2ad59d0e0a243d40017ad.png)

输入2以后,会将output/proxy.txt中的代理,进行批量验证,最终保存到output/http.txt文件当中.

![](https://pic1.imgdb.cn/item/67b2ada1d0e0a243d40017c5.png)

---

# :factory::验证自己的代理

我们除了可以验证使用1参数生成的代理,也可以用来验证自己的代理池ip,

首先,我们需要打开output,文件夹

![](https://pic1.imgdb.cn/item/67b2adfad0e0a243d40017d0.png)

里面存放了两个文件,分别为proxy.txt和http.txt

我们将自己的代理存放在proxy.txt文件当中,一行一个,如下图所示:

![](https://pic1.imgdb.cn/item/67b2ae35d0e0a243d40017e2.png)

存放完成后,保存,运行fifa0.exe

选择'2'参数,运行即可,最终可以使用的代理池,则会存放在http.txt中.

![](https://pic1.imgdb.cn/item/67b2aeccd0e0a243d4001802.png)

则验证成功

----

# :walking::开始切换ip

![](https://pic1.imgdb.cn/item/67b2af11d0e0a243d400181e.png)

输入'3'即可开始切换代理ip,切换ip速度,取决了config/conf.txt中的get_time参数

![](https://pic1.imgdb.cn/item/67b2af53d0e0a243d4001839.png)

![](https://pic1.imgdb.cn/item/67b2af67d0e0a243d4001845.png)

![](https://pic1.imgdb.cn/item/67b2af9bd0e0a243d4001874.png)

如果需要停止,则使用CTRL+C即可停止

---

# :zap::使用自己的ip池进行切换

我们只需要把自己的ip存放在output.txt中,再运行 参数 '3',即可进行ip切换



# 

# :satisfied:FiFa0-Pro

FiFa0-Pro是Fifa0的一个付费版本,可以用户免去配置,以及提供一个永久性的key,让用户体验到高端的且牛逼的一款代理池ip切换工具

FiFa0-Pro是在Fifa0的基础上,进行了进一步优化,和更多的功能,同时操作方式与Fifa0也略有不同



# :satisfied:FiFa0-Pro教程

首先从作者这里购买FiFa0-Pro版本以后,解压到文件夹,并打开终端,

WIndows11,可以直接在FiFa0-Pro版本的目录下右键,从终端打开,

![](https://pic1.imgdb.cn/item/67b2b183d0e0a243d400192b.png)

WIndows10可以在目录框中,输入CMD或powershell,进行打开,

![](https://pic1.imgdb.cn/item/67b2b203d0e0a243d4001954.png)

----

打开终端后:

运行:fifa-Pro -h

![](https://pic1.imgdb.cn/item/67b2b383d0e0a243d40019a4.png)

即可显示参数

----

从参数中我们可以看到,付费版多出了好些参数,

自动验证ip参数\指定验证ip池参数\获取指定地域的ip信息\更换ip切换速率\单独的验证ip\保存ip池\以及更新等多个参数.

# :1st_place_medal::基本使用方式

```
# 如果情况紧急,请直接使用 -A参数
fifa-pro -A #会运行整套功能,并自动开启ip切换

# 获取帮助
fifa0-pro -h

# 获取ip池
FiFa0-pro -f

# 验证ip是否能用
fifa0-pro -VO

# 验证自己的ip池是否可用
fifa0-peo -V [自己的ip池txt文件路径] -O [要保存的位置] #注意,此处的-O保存位置,只需要写路径即可,例如/'D:\tools\筛选\'不需要带有文件名称

# 验证ip池,并保存到output目录中的http.txt文件
fifa0-pro -V [ip池txt文件路径]

# 切换ip更换速度
fifa0-pro -R [速度]  #例如:0.2等于0.2秒

#获取不同地区的ip池
fifa0-pro -fi [参数] #目前fi参数支持:US(美国),SG(新加坡),KR(韩国),(HK)香港

#更新软件版本
fifa0-pro -up

#开始切换ip
fifa0-pro -S
```

# :o::常见报错

![](https://pic1.imgdb.cn/item/67b2ba05d0e0a243d4001a8b.png)

网络出现问题了,检查网络后再进行下载.

---

如果QQ\微信有网络,但是浏览器没有网络,请运行

fifa0-pro -S 后再运行 CTRL+C 停止,即可回复网络

---

如果提示:未选择参数,

![](https://pic1.imgdb.cn/item/67b2baded0e0a243d4001aaa.png)

那么请使用fifa0-pro -h 进行参数查看

---

运行之后闪退

请在终端中运行即可.

---

如果还有报错,请及时联系:Yancy_76或者QQ323002946

