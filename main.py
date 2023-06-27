import re
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QTimer
from atexit import register
from os.path import isfile
from pickle import dump, load

if not isfile("users"):
    with open("users", "w") as f:
        pass

if not isfile("messages"):
    with open("messages", "wb") as f:
        dump([], f)

class Message:
    def __init__(self, user, content):
        self.user = user
        self.content = content
    
    def __repr__(self):
        return f"Message({self.user}, {self.content})"

    def __str__(self):
        return f"{self.user}: {self.content}"

    def info(self):
        return (self.user, self.content)

form_class = uic.loadUiType("ThisChat.ui")[0]

class ThisChat(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        register(lambda: self.del_user(self.username))
        self.set1 = [
            self.label1,
            self.label2,
            self.now,
            self.sendmsg,
            self.tb,
            self.name,
            self.users
        ]
        self.set2 = [
            self.label3,
            self.uncf,
            self.un
        ]
        for each in self.set1:
            each.setVisible(False)
        self.sendmsg.clicked.connect(self.send)
        self.uncf.clicked.connect(self.confirmUsername)
        self.username = None
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateAll)
        self.timer.start(1000)

    def send(self):
        text = self.now.text().rstrip()
        if text.startswith("/"):
            temp = re.match(r"^/ban @(.*?);$", text)
            if temp:
                user = temp.group(1)
                self.ban(user)
        self.add_message(self.username, text)

    def confirmUsername(self):
        username = self.un.text().strip()
        if username == '' or username in self.get_users():
            return
        for each in self.set1:
            each.setVisible(True)
        for each in self.set2:
            each.setVisible(False)
        self.username = username
        self.name.setText(username)
        self.add_user(username)

    def ban(self, user):
        if user in self.get_users():
            self.del_user(user)
            self.add_message("Robot", f"✅User banned: {user}")
        else:
            self.add_message("Robot", f"❌User does not exist")

    def add_user(self, username):
        users = self.get_users()
        with open("users", "w", encoding="utf-8") as f:
            users.append(username)
            f.write("\n".join(users))

    def get_users(self):
        with open("users", "r", encoding="utf-8") as f:
            users = f.read().splitlines()
            return users
    
    def del_user(self, username):
        try:
            users = self.get_users()
            users.remove(username)
            with open("users", "w", encoding="utf-8") as f:
                f.write("\n".join(users))
        except:
            pass
    
    def add_message(self, username, content):
        message = Message(username, content)
        messages = self.get_messages()
        messages.append(message)
        with open("messages", "wb") as f:
            dump(messages, f)
    
    def get_messages(self):
        with open("messages", "rb") as f:
            return load(f)

    def update_userlist(self):
        users = [each.rstrip("\n") for each in self.get_users()]
        self.users.clear()
        for user in users:
            self.users.append(user)
    
    def update_messages(self):
        messages = self.get_messages()
        self.tb.clear()
        for message in messages:
            info = message.info()
            self.tb.append(f"<b><span style='color: green;'>{info[0]}</span></b>:")
            self.tb.append(f"<span style='color: black;'>{info[1]}</span>")
    
    def check_ban(self):
        if self.username and self.username not in self.get_users():
            self.close()

    def updateAll(self):
        self.check_ban()
        self.update_userlist()
        self.update_messages()

if __name__ == "__main__":
    app = QApplication([])
    thischat = ThisChat()
    thischat.show()
    app.exec()
