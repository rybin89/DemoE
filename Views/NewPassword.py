from tkinter import *
from tkinter import ttk
from Controllers.UserController import UserController

class NewPassword(Tk):
    def __init__(self,user):
        super().__init__()
        self.user = user

        # конфигурация окна
        self.title("Смена пароля при первом входе")
        self.geometry("500x500")

        # Старый пароль
        self.old_password = ttk.Label(self,text="Введите пароль")
        self.old_password.pack(anchor="center")
        #окно ввода Старый пароль
        self.old_password_input = ttk.Entry(self)
        self.old_password_input.pack(anchor="center")
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

    def button_clicked(self):
        # Добавить метод авторизация
        # Если метод вернёт True - сообщение
        # Если метод вернёт False - сообщение
        self.old = self.old_password_input.get()
        self.new = self.new_password_input.get()
        if self.old == self.user.password:
            UserController.update_all(self.user.id, password = self.new, first_auth = 0)
        else:
            self.message['text'] = "Вы ввели неверный пароль"


if __name__ == "__main__":
    window = NewPassword()
    window.mainloop()