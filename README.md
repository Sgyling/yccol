# fifa0
基于fofa编写的一款代理池工具
---
title: fifa0-基于fofa的全自动代理池更换工具
date: 2025-02-09 15:46:40
tags: 代理池
categories: 渗透
---

链接：https://pan.quark.cn/s/e88d195e4049


## 一、开发者

这只是一个通过fofa获取代理的软件,且支持验证自己的ip库.

## 二、功能概述

FIFA0 基于 Fofa 搜索引擎，实现了信息收集过程中寻找、验证与更换等操作的全程自动化。无论是网络安全研究人员对特定目标的信息挖掘，还是运维人员对自身网络资产的梳理，该工具都能极大提高工作效率。

1. **目标爆破**：该工具可自动爬取fofa相关代理信息,并进行自动切换,用于目标爆破拥有非常可观的效果.
2. **~爬虫~**：~该工具可进行对ip封禁的网站进行爬取,由于自动切换ip的功能,以让爬虫可以无休止不间断的爬取.
3. **等...**：该工具用法非常简单,傻瓜式的操作,可用于多种红队,或其他不同的场景

## 三、工具和教学

### 1.获取代理
- 在config目录里conf.txt中配置fofa的key即可.
- 运行1即可
- 运行完成后,即保存到output目录中的http.txt中
### 2.代理验证
- 代理验证可以单独验证自己的代理,
- 运行之前只需要把自己的ip存放在output目录中的proxy.txt(需要一行一个)
- 存放完成后保存.
- 保存后,运行软件,执行'2'参数即可
- 最后可用代理会存放在:output目录中的http.txt中
### 3.开启代理
- 在config目录的conf.txt里更改get_time=''中的参数,即可设置代理ip切换速度
- 设置完ip切换速度后,运行此软件,运行3即可
- 则会按照设置的速度进行更换ip
- 注:此处切换的ip地址为:output文件夹里的http.txt
- 如果需要运行自己的ip,直接讲http.txt中数据进行更换即可.
### 4.全自动操作
- 运行之前需要先配置进行配置,将config中的conf.txt添加上fofa的key和代理ip切换键时间time
- 全自动进行操作,并且会自动开启切换ip

## 四、下载安装
'''
   # 方法1: 找到文章最开始的链接,保存到网盘,进行下载.
   # 方法2:
   git clone https://github.com/Sgyling/fifa0
   cd fifa0
   fifa.exe
'''

## 五、常见错误

![](https://pic1.imgdb.cn/item/67a865d7d0e0a243d4fd4ac9.png)

这种情况一般是conf.txt中没有添加fofa的key,或者key不正确

----

![](https://pic1.imgdb.cn/item/67a86628d0e0a243d4fd4af3.png)

这种情况一般是没有conf.txt中没有添加更换时间,或者是里面有空格,

----



## 五、版本与付费策略


1. **免费版本**：具备付费版本的所有核心功能，为广大用户提供了零门槛体验 FIFA0 强大功能的机会。然而，免费版本需要用户自行进行配置，这要求使用者具备一定的技术基础与操作经验。通过自行配置，用户能够深入了解工具的运行机制，灵活调整参数以满足个性化需求。

2. **付费版本**：
   - **Key 提供**：付费后，用户将获得相关的 key，免去自行配置的繁琐过程，即装即用，大大节省时间与精力。这些 key 经过优化与定制，能够使工具在运行时达到最佳性能状态。
   - **整体质量提升**：付费版本在稳定性、响应速度等方面进行了深度优化，为用户带来更加流畅、高效的使用体验。无论是大规模数据的处理，还是长时间的连续运行，付费版本都能保持出色的表现。
   - **多种额外功能**：付费版添加上了不同地域的ip代理池获取,当前包含:美国\韩国\中国\香港\新加坡等,对IP进行了划分,并且免去配置,开箱即用,包括代理ip切换速率,也进行了集合,无需进行手动配置
3.**功能对比**
左边为:付费版,右边为:免费版

![image](https://github.com/user-attachments/assets/76cd1456-1a1f-4479-b766-913138ed7259)

![image](https://github.com/user-attachments/assets/bb2f5746-3a35-4ef9-ada5-cf9312373029)

----

视频对比付费版和免费版的区别:B站:疯狂的杨CC


github:https://github.com/Sgyling/fifa0

# FIFA0 工具法律责任声明

​		1.**合法使用承诺**：用户在使用由 B 站 up 主 “疯狂的杨 CC” 开发的 FIFA0 工具前，应详细阅读并理解本声明。使用该工具即表明用户承诺其使用行为严格遵守中华人民共和国以及其他相关国家和地区的所有适用法律法规，包括但不限于网络安全法、数据保护法等。

​		2.**违法责任自负**：若用户利用 FIFA0 工具进行任何违法违规活动，包括但不限于未经授权的网络扫描、数据窃取、恶意攻击等，由此引发的一切法律后果，包括但不限于刑事指控、民事赔偿责任以及行政罚款等，均由用户自行承担，与工具开发者 “疯狂的杨 CC” 以及工具发布平台（如 B 站）无任何关联。开发者保留追究因用户违法使用行为给自身造成损失的权利。

​		3.**知识产权保护**：用户不得对 FIFA0 工具进行反向工程、反编译、拆卸或任何试图获取工具源代码及核心算法的行为，除非已获得开发者明确的书面授权。若用户违反此规定，将承担相应的知识产权侵权责任，包括但不限于停止侵权行为、消除影响、赔偿开发者因此遭受的全部损失。

​		4.**第三方责任**：若因用户使用 FIFA0 工具导致对任何第三方的合法权益造成损害，用户应独自承担所有法律责任和赔偿义务，保证工具开发者及相关平台免受任何第三方的索赔、诉讼或其他法律程序的牵连。

​		5.**责任豁免**：在任何情况下，工具开发者 “疯狂的杨 CC” 对用户因使用或无法使用 FIFA0 工具而产生的任何直接、间接、偶然、特殊或后果性的损失，包括但不限于数据丢失、业务中断、利润损失等，均不承担任何责任，无论该责任是基于合同、侵权、疏忽或其他法律理论。


