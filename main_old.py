from tkinter import *
from datetime import datetime

def fas():
    """
    发送消息
    :return: None
    """
    text = sendmsg.get(1.0, END).rstrip()
    # 清空
    sendmsg.delete(1.0, END)
    messages.append(text)
    msg["state"] = NORMAL
    now = datetime.now()
    # 类似于 html 的 class 属性，便捷地设置标签
    msg.insert(END, f"{username}", "user")
    msg.insert(END, f" 发表于 {now.strftime('%Y-%m-%d %H:%M:%S')}", "time")
    msg.insert(END, "\n")
    msg.insert(END, text)
    msg.insert(END, "\n\n")
    msg["state"] = DISABLED
    sendb["state"] = DISABLED

def check(ev):
    """
    检查
    :param ev: event(from tk)
    :return: None
    """
    if sendmsg.get(1.0, END).strip():
        sendb["state"] = NORMAL
    else:
        sendb["state"] = DISABLED

def change():
    """
    更改用户名，差不多就是切换用户
    :return: None
    """
    func = lambda: changeto(entry, top)
    top = Toplevel()
    top.title("输入你的新用户名")
    top.geometry('300x50+150+150')
    entry = Entry(top, font=font)
    entry.grid(row=0, column=0)
    cfm = Button(top, text="确定(Enter)", font=font, width=10, height=1)
    cfm["command"] = func
    cfm.grid(row=0, column=1)
    top.bind("<KeyPress-Return>", lambda x: func())
    top.mainloop()

def changeto(entry, top):
    global username
    username = entry.get()
    top.destroy()
    uss["text"] = f"当前用户名：{username}"

# 消息
messages = []

root = Tk()
root.geometry("700x700+100+100")
root.title("This Chat V1.0 - Powered by dddddgz")

# 通用的字体
font = ("Microsoft Yahei UI", 11)

# 用户名
username = "TestUser"

# username shower
uss = Label(root, text=f"当前用户名：{username}", font=font)
uss.grid(row=1, column=1)

# username editor
use = Button(root, text="更改用户名", font=font)
use["command"] = change
use.grid(row=1, column=2)

label = Label(root, text="历史消息", font=font)
label.grid(row=1, column=0, sticky=W)

# 历史消息
msg = Text(root, width=50, height=20, font=font)
msg["state"] = DISABLED
msg.tag_config("user", foreground="green", font=font + ("bold", ))
msg.tag_config("time", foreground="blue", font=font)
msg.grid(row=2, column=0)

label = Label(root, text="发送消息", font=font)
label.grid(row=3, column=0, sticky=W)

# 消息编辑区
sendmsg = Text(root, width=50, height=4, font=font)
sendmsg.grid(row=4, column=0)

# 消息发送按钮
sendb = Button(root, width=20, height=1, font=font, text="发送消息(Ctrl+Enter)")
sendb["command"] = fas
sendb["state"] = DISABLED
sendb.grid(row=4, column=1, sticky=W, columnspan=2)

# 每次一按下键就检测是否应该更改 sendb 的状态为 NORMAL 或 DISABLED
root.bind("<KeyPress>", check)

root.bind("<Control-KeyPress-Return>", lambda x: fas())
root.mainloop()
