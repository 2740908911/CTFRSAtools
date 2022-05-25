# CTFRSAtools


## 摘要

* 该工具定位于CTF比赛中Crypto方向中RSA类型题目的自动判断、分析与解题。

* CTFRSAtools(下文简称CRts)支持脚本扩充，可以将比赛中遇到的其他脚本及时补充至CRtss工具中。事实上，CRts只是作为一个RSA脚本容器存在，并集成了部分CTFCrypto中rsa题型常见工具，您可以通过自行添加、补充甚至更改脚本的方式自定义CRts。本工具已经加入了常见题型的脚本近20个，可以满足大部分比赛的基础格式RSA类型题目，如果您需要扩充脚本，请注意脚本的格式需参照其他脚本文件。脚本的扩容会在下文详细介绍。

* CRts没有加入segamath脚本，因此像有限域开方、CopperSmith明文高位攻击、Franklin-Reiter攻击、多项式等类型的题目，还请师傅手撸吧。

* CRts支持公钥分解、文件解密，具体使用方法见下文。

* 使用说明、其他问题及帮助详见下文。



## 结构与思路

**CRts结构**

```
CTFRSAtools
/example	# data.txt案例
	--略
/RSAtools	# 脚本储存、调用
	--略
--banner.py
--main.py
--RSAjudge.py	# 在此处添加识别信息

附
data.txt	# 题目数据
flag.enc	# 解密文件
pub.key		# 公钥文件
readme.md	# 文件说明
```

**设计思路：**

​		CRts作为一个解题容器，采用脚本和判断分离的方式，可以最大化保障工具的自定义能力。

​		CRts采用data.txt方式读取数据而非命令行输入，可以保障数据的反复可阅且容易修改检查。

​		CRts需要python3版本的支持，搭建的版本为python3.8，使用时请注意库的安装。

​		



## 功能与注意

**功能：**

```
# 功能会随着版本的更新不断增改，以CRts实际运行效果为准。
# 每次比赛后都可能会添加脚本，若有新的想法，可以联系作者加入github项目组共同开发
# 功能示例见<使用与测试>

+ 标准类型的RSA题型互解(详略)
+ 基与factordb.com和yafu的大数分解
+ dp泄露攻击
+ dp、dq泄露攻击
+ 共模攻击
+ 低解密指数攻击(e较大)
+ 维纳攻击
+ 公钥分解
+ 文件解密

```

**注意：**

1. 由于分解N时会用到factordb，故需要连接网络；若无网络连接，将使用yafu分解，在面临大数时效率可能过低。您也可以自行在factordb.com或yafu分解后，写入data.txt。
2. segamath暂时没有配备到CRts中，故sega类脚本无法加入脚本集。
3. 有些功能可能不完善，为了避免不必要的错误，请尽量确保data.txt中的每个值都是有用的。
4. 在使用该工具时，应当有一定的RSA基础，在解题时如果有bug，可以根据分析调整甲苯，并请及时反馈。



## 下载与安装

**下载：**

CRts暂未开源（还在不断的完善脚本，等效果很好了再放出，目前只能解简单题）

CRts已托管至github，有兴趣的师傅可以联系作者，协同开发。

**安装：**

```
1. git clone 或 download 

2. 安装python3 （有请略）

3. pip install gmpy2

4. pip install Crypto

5. pip install RSA

6. pip install numpy

7. 缺啥库补啥。。。

8. 运行测试
```

安装中有问题请参考百度（3、4等）

预期在开源后发布exe版本（注：exe版本可能无法自定义脚本）



## 使用与测试

**使用说明：**

1.  使用前请确保数据已在CRts根目录中写入data.txt或存入pub.key/flag.enc文件
2.  打开cmd 或 powershell，cd至CRts根目录
3.  `python main.py`
4.  脚本自动运行后，等待结果返回即可，若无结果或有bug，请与作者联系
5.  请调用完成后及时清除data.txt、pub.key、flag.enc文件，以便下一次使用

**测试示例：**

> 示例选取的题目数据均来自于CTFshow与buuCTF
>
> 以下展示示例为乱序，与功能顺序无关。

<!--p-->

![b9b5225684d4f0a1c1dab39aa492ae6f.png](http://img.imfanqie.xyz/images/2022/05/25/b9b5225684d4f0a1c1dab39aa492ae6f.png)

![7e02342279d2641abc7bc54c92c9ed6a.png](http://img.imfanqie.xyz/images/2022/05/25/7e02342279d2641abc7bc54c92c9ed6a.png)

![ec274f31481dfed3a503fe11eed37614.png](http://img.imfanqie.xyz/images/2022/05/25/ec274f31481dfed3a503fe11eed37614.png)

![61ffc40146d6d83dee5511fbfa97d945.png](http://img.imfanqie.xyz/images/2022/05/25/61ffc40146d6d83dee5511fbfa97d945.png)

![52ceae63a122db7c49ca637cc0f0549c.png](http://img.imfanqie.xyz/images/2022/05/25/52ceae63a122db7c49ca637cc0f0549c.png)

![54aab50011f3a9d9bc9d5b0bb818f8aa.png](http://img.imfanqie.xyz/images/2022/05/25/54aab50011f3a9d9bc9d5b0bb818f8aa.png)

![e734dd9a4caf01462a617b0af59cdeec.png](http://img.imfanqie.xyz/images/2022/05/25/e734dd9a4caf01462a617b0af59cdeec.png)

![48e37229d386fa9425615eab652fc3ca.png](http://img.imfanqie.xyz/images/2022/05/25/48e37229d386fa9425615eab652fc3ca.png)

![37c0ded11a20d6dbd7febafb3720d782.png](http://img.imfanqie.xyz/images/2022/05/25/37c0ded11a20d6dbd7febafb3720d782.png)



## 自定义扩展

> 使用该方法时请确保您对RSA类型题目有一定的了解，并且已经参考过RSAtools中的其他脚本。

如果您需要自定义脚本（删除修改以及添加），您可以参考以下部分。

* 请提前查看RSAtools中的其他脚本：

  * 这里以大多数文件的格式举例：
       	solves()函数将作为解决问题的基本接口函数，以便于被其他脚本调用
       	printf()函数作为打印值函数，调用solves()进行计算，并返回于屏幕
  * 调用其他脚本的格式为 `from RSAtools import xxxxx`
  * 若计算结果为d，可以参考如下格式：

  ```python
  def printf(e,p,q):
      d = solves(e,p,q)
      print("=" * 99)
      print("int_d：" + str(d))
      print("=" * 99)
  ```

  * 若计算结果为m，可以参考如下格式：

  ```python
  def printf(x,y,z):
  	m = solves(x,y,z)
  	print("=" * 99)
  	try:
  		print("int：" + str(m))
  		print("hex：" + str(hex(m)))
  	except:
  		print("int：" + str(m))
  
  	try:
  		print("hex to ascii：" + str(binascii.unhexlify(hex(m)[2:])))
  	except:
  		try:
  			print("libnum(n2s)：" + str(libnum.n2s(hex(m))))
  		except:
  			print("just hex or int ")
  	print("=" * 99)
  ```

* 根据格式写好新脚本后，将判断条件加入RSAjudge.py

  + 在fun_call()函数中，您能看到所有的方法调用，当您补充脚本时，也可以加入该函数以便使用。
  + 在judge(RSAdata)函数中，你可以根据print和注释得出数据分类情况，将您的脚本加入相应的类别中即可。

+ 如果您有新的元素要定义，例如r、x、y、z等 可以参考main.py中的写法另赋值即可。



## 版本及更新

**版本日志**

| 名称        | 版本     | 日期      | 日志and备注                  |
| ----------- | -------- | --------- | ---------------------------- |
| CTFRSAtools | beta 0.1 | 2022.5.24 | 基带版本，后续更新时间看情况 |
|             |          |           |                              |
|             |          |           |                              |

**计划目标**

* 加入sega脚本
* 扩充RSA解题范围，加入其它类型题目求解法
* 整合其它密码类型，扩展tools应用范围，如：base家族，进制转换，编码转换，md5定向爆破等
* 待定……



## 结尾

本文档基于初代版本而写，因更新原因，可能会与实际产品有所差异，本说明仅供参考。

该项目仅供学习和比赛使用，未经允许禁止私自传播分享！

同时欢迎其他师傅加入开发共同完善，项目库未公开，项目地址请联系作者。

> 作者：Fanqie
>
> 联系方式：q/v 2740908911
>
> 最后编辑时间：2022/5/25
