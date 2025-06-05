from tkinter import *
from tkinter import ttk

from Controllers.UserController import UserController



class EditView(Tk):
    def __init__(self,login):
        super().__init__()
        self.login = login
        #Получить пользователя
        self.user = UserController.show_login(self.login)
        # конфигурация окна
        self.title(f"Редактирование пользователя {self.user.fullname}")
        self.geometry("500x500")

        # Старый логин
        self.new_login = ttk.Label(self, text="Введите новый логин")
        self.new_login.pack(anchor="center")
        # окно ввода новый логин
        self.new_login_input = ttk.Entry(self)
        self.new_login_input.pack(anchor="center")
        # Новый Пароль
        self.new_password = ttk.Label(self, text="Введите новый пароль")
        self.new_password.pack(anchor="center")
        # окно ввода ПаролЯ
        self.new_password_input = ttk.Entry(self, show='*')
        self.new_password_input.pack(anchor="center")
        # сообщение
        self.message = ttk.Label(self)
        self.message.pack(anchor="center")

        # определение кнопки
        self.button = ttk.Button(self, text="Изменить")
        self.button["command"] = self.button_clicked
        self.button.pack(anchor="center", expand=1)
        # определение кнопки
        self.button = ttk.Button(self, text="Разблокировать")
        self.button["command"] = self.button_ban
        self.button.pack(anchor="center", expand=1)
    def button_clicked(self):
        # Добавить метод авторизация
        # Если метод вернёт True - сообщение
        # Если метод вернёт False - сообщение
        self.log = self.new_login_input.get()
        self.pas = self.new_password_input.get()
        if self.log != "":
            UserController.update_all(self.user.id, login = self.log)
        if self.pas != "":
            UserController.update_all(self.user.id, password = self.pas)

        self.destroy()
    def button_ban(self):
        UserController.update_all(self.user.id,ban=False)
