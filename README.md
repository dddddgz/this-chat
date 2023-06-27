# This Chat

## 简介

This Chat V1.0 请见：[传送门](https://fishc.com.cn/thread-229817-1-1.html)

This Chat V1.0 采用的是 tkinter，但 tkinter 并不是 Windows 标准 GUI。

This Chat V1.1 进行了这方面的考虑，将 GUI 改成了 PyQt6。

目前你看见的就是 PyQt6 版的 This Chat。

## 更新日志

- V1.1 最新版本（当前版本）

- [V1.0](https://github.com/dddddgz/this-chat/commit/4adfd2c9c1b0dd2942acb7d00607239f66d68214) 初次创建

## 运行准备

```powershell
pip install PyQt6 -i https://mirrors.aliyun.com/pypi/simple
```

pip 源永久设置：

```powershell
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple
pip config set install.trusted-host mirrors.aliyun.com
```

## 代码解释


![](https://dddddgz.github.io/1/1.png)

1. 导入正则表达式库 re

2. 导入 PyQt6 的 uic，`uic.loadUiType()` 方法可以加载 Qt GUI 文件（.ui），搭建 Qt GUI 推荐使用 Qt Designer（[传送门](https://build-system.fman.io/qt-designer-download)）

3. 加载 PyQt6 必要部件（PyQt6 固定用法）

4. 导入 PyQt6 计时器

5. 导入 `atexit.register()` 函数，用于设置程序正常退出（即点击 PyQt6 窗口的关闭按钮后）执行的函数或方法

6. 从 `os.path` 导入 `isfile`，用于判断是否有某个文件

7. 从 `pickle` 导入 `dump` 和 `load`，`dump` 表示写入二进制文件，`load` 表示从二进制文件中导入内容

![](https://dddddgz.github.io/1/2.png)

9. 判断 `users` 文件是不是不在（This Chat V1.1 中的用户列表文件，文本类型）
10. 新建 `users` 文件（文本文件）
11. 啥也不写

13. 判断 `messages` 文件是不是不在（This Chat V1.1 中的消息列表文件，二进制文件类型）
14. 新建 `messages` 文件（二进制文件）
15. 给 `messages` 文件写入一个空列表

![](https://dddddgz.github.io/1/3.png)

17. 定义 `Message` 类，用于表示一条消息
18. 初始化方法，`user` 是用户名，`content` 是用户发送的内容
19. 设置用户名到 `Message` 对象的属性
20. 设置内容到 `Message` 对象的属性

22. 定义 `__repr__` 方法
23. 设置 `__repr__` 方法返回类似于 `Message(who, what)` 的内容（`str` 类型）

25. 定义 `__str__` 方法
26. 设置 `__str__` 方法返回类似于 `who: what` 的内容（`str` 类型）

28. 定义 `info` 方法
29. 设置 `info` 方法返回类似于 `(who, what)` 的内容（`tuple` 类型

![](https://dddddgz.github.io/1/4.png)

31. 导入 Qt GUI 并赋值给 `form_class`，`form_class` 是 GUI 需要继承的类

33. 定义 `ThisChat`（主程序窗口）类
34. 定义 `__init__` 方法
35. 调用 `super().__init__(self)`
36. Setup UI（UI 和 GUI 的区别：[传送门](https://worktile.com/blog/know-1451)）

![](https://dddddgz.github.io/1/5.png)

37. 调用 `atexit.register()` 方法，设置在程序退出时，在用户列表里删除自己

38-46. 创建 `set1` 列表，里面是在聊天页面所用到的控件

47-51. 创建 `set2` 列表，里面是在设置用户名页面所用到的控件

52. 遍历 `set1`
53. 调用控件的 `setVisible()` 方法，隐藏聊天页面控件

![](https://dddddgz.github.io/1/6.png)

54. 将用于发送信息按钮 `sendmsg` 与 `send()` 方法绑定
55. 将用于确认用户名的按钮 `uncf` 与 `confirmUsername()` 方法绑定
56. 设置自己的用户名为 `None` （未设置）
57. 创建一个 PyQt6 计时器（`QTimer` 类）
58. 设置计时器事件到时执行 `updateAll()` 方法
59. 设置计时器每 1000 毫秒执行函数

![](https://dddddgz.github.io/1/7.png)

61. 定义 `send()` 方法
62. 获取输入的消息并清除右部字符
63. 判断消息是否以 `/` 开头
64. 通过[正则表达式](https://dddddgz.github.io/zhengze.html)判断是否输入了 ban 命令（例如，`/ban @who;`）
    - ^ 表示开头，$ 表示结尾，也就是说判断的就是中间一部分 `/ban @(.*?)$`
    - `/ban @` 和 `;` 是普通的文本
    - `(.*?)` 表示一个组，`.*?` 表示非贪婪匹配，就是一直往后找，但是找到一个
65. 如果是的话，`temp` 变量就不是 None，可以通过 if 判断
66. 通过 `group()` 方法获取匹配（1 表示第一个）
67. `ban` 这个用户
68. 将自己的消息原样发出去

![](https://dddddgz.github.io/1/8.png)

70. 定义 `confirmUsername()` 方法
71. `un` 为用户名输入框，获取输入框里的文字，然后清除空字符

72-73. 如果用户名为空或已经存在，直接退出函数

74-75. 将 `set1` 里的内容全部显示

76-77. 将 `set2` 里的内容全部隐藏

78. 设置自己的 `username` 属性为输入的用户名
79. 将用户名显示在 `name` 上
80. 将自己添加到用户列表

![](https://dddddgz.github.io/1/9.png)

82. 定义 `ban()` 方法，用于删除用户
83. 如果这位用户存在
84. 就把他从用户列表里删掉
85. 让机器人发送成功的消息
86. 否则
87. 让机器人发送失败的消息

![](https://dddddgz.github.io/1/10.png)

89. 定义 `add_user()` 方法，用于添加用户
90. 首先获取用户列表
91. 以写模式打开用户列表文件，编码 utf-8
92. 在 `users` 列表里添加新用户

93. 将 `users` 列表用换行符拼接，并写入用户列表文件

![](https://dddddgz.github.io/1/11.png)

95. 定义 `get_users()` 方法，用于获取用户列表
96. 以读模式打开用户列表文件，编码 utf-8
97. 读取用户列表文件的全部内容，然后按换行符拆分

97. 返回读取到的用户列表

![](https://dddddgz.github.io/1/12.png)

100. 定义 `del_user()` 方法，用于删除用户
101. 使用 try-except 结构，为了在用户不存在时啥也不做
102. 获取用户列表
103. 在 `users` 列表里删除指定的用户名
104. 以写模式打开用户列表文件，编码 utf-8
105. 将 `users` 列表用换行符拼接，并写入用户列表文件
106. 如果出错
107. 啥也不干

![](https://dddddgz.github.io/1/13.png)

109. 定义 `add_message()` 方法
110. 将要发的信息变成 `Message` 类
111. 获取消息列表
112. 在 `messages` 列表里添加新消息
113. 以写模式+二进制模式打开信息列表文件
114. 将 `messages` 列表写入信息列表文件里

![](https://dddddgz.github.io/1/14.png)

116. 定义 `get_messages()` 方法，用于获取消息列表
117. 以读模式+二进制模式打开消息列表文件
118. 返回从消息列表文件中提取的内容

![](https://dddddgz.github.io/1/15.png)

120. 定义 `update_userlist()` 方法，用于更新 PyQt6 窗口里显示的用户列表
121. 获取所有用户（这里当时改了 `get_users()` 后没删掉，现在既然代码已经公布了 -> [传送门](https://fishc.com.cn/thread-230010-1-1.html)，那就等 1.2 再改吧，到时候改成 `self.get_users()`）
122. 清除 `users` 控件里的内容
123. 遍历用户列表
124. 将用户一行行地写入控件里

![](https://dddddgz.github.io/1/16.png)

126. 定义 `update_messages()` 方法，用于更新 PyQt6 窗口里显示的消息列表
127. 获取所有消息
128. 清空 `tb` 空间里的内容
129. 遍历消息列表
130. 通过 `info()` 方法获取该消息的发布者和内容
131. 将发布者信息变成绿色加粗字体，并附加一个 `:`，写入控件
132. 将内容变成黑色字体，写入控件

![](https://dddddgz.github.io/1/17.png)

134. 定义 `check_ban()` 方法
135. 如果自己的用户名不为空（即已经输入过用户名）且自己不在用户列表里（因为做不到关闭其他用户的窗口，所以只能设定某种标志，然后让每个窗口去检查）
136. 那么自己就被 ban 掉了

![](https://dddddgz.github.io/1/18.png)

138. 定义 `updateAll()` 方法，用于一次性调用所有需要一直执行的函数（类似于 PyGame 主循环，不过 QTimer 这里设置的时间是 1000 毫秒，所以运行相对慢一点，但是如果没有动画展示的话，PyQt6 版的 This Chat 和 PyGame 版的 This Chat 就没啥区别了）
139. 调用 `check_ban()` 方法，检查有没有被 ban 掉
140. 调用 `update_userlist()` 方法， 更新用户列表
141. 调用 `update_messages()` 方法， 更新消息列表

![](https://dddddgz.github.io/1/19.png)

143. 经典主程序判断
144. 创建一个 `QApplication` 的实例化对象
145. 创建主程序的类
146. 显示窗口
147. 当上一行运行完成就说明窗口被关闭了，所以 `app` 也要退出

## Hacker 指南

嗯，作为一名合格的 Hacker，只会玩 GUI 界面是不够滴！

让我们来看看该怎么乱改：

- 可以直接在用户列表文件里删用户
- 更改 `update_messages()` 方法里发布者和内容的颜色、字体

