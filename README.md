## cqooc.com_AutomaticLearnCourse
**重庆高校在线开放课程平台_自动学习课程**

首先感谢 [@qnnnnez](https://github.com/qnnnnez) 提供的源码

[这是源代码](https://gist.github.com/qnnnnez) | gist.github.com 被墙，需要fq才能使用

#### 使用之前
+ 添加 Chrome扩展 [EditThisCookid](https://chrome.google.com/webstore/detail/editthiscookie/fngmhnnpilhplaeedifhccceomclgfbg/reviews)
+ 拥有一个 [cqooc.com | 重庆高校在线开放课程平台 ](http://www.cqooc.com/login) 账号
+ 必须安装 Python requests 模块
+ python 3 | 推荐 Python 3.6.5

requests 模块安装方式: 

`python -m pip install --upgrade pip`

`pip install requests`

### 配置文件

+ `username = '' ` 单引号里面填写登录账号 例如 10611xxxxxxx

+ `user_id=int() ` 不清楚，可省略

+ `courseId = ''`  刷课的课程ID，在个人主页-进入学习里面，例如 `http://www.cqooc.com/learn/mooc?id=334565517&cid=11514410` courseID 就是 334565517

+ `cookie_xsid = '' ` 这里就需要使用 EditThisCookid 扩展,登录帐号之后-点击图标-找到 xsid 这一项，复制值放到单引号里面 ![](http://ww1.sinaimg.cn/large/005IuAdyly1g37mon30ezj30fd0d8wet.jpg)

+ `finish_time = '' `  完成时间，可省略,建议当天时间

+ `parentId = '' ` 不清楚,可省略

### 完成图

![](http://ww1.sinaimg.cn/large/005IuAdyly1g37mm0orc7j30j604j3yi.jpg)
