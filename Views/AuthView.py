
from tkinter import *
from tkinter import ttk

from Controllers.UserController import UserController
from Views.AdminViews import AdminView
from Views.NewPassword import NewPassword


class AuthView(Tk):
    def __init__(self):
        super().__init__()

        # конфигурация окна
        self.title("Вход в систему Отеля")
        self.geometry("500x500")

        # Логин
        self.login = ttk.Label(self,text="Логин")
        self.login.pack(anchor="center")
        #окно ввода логина
        self.login_input = ttk.Entry(self)
        self.login_input.pack(anchor="center")
        # Пароль
        self.password = ttk.Label(self, text="Пароль")
        self.password.pack(anchor="center")
        # окно ввода ПаролЯ
        self.password_input = ttk.Entry(self, show='*')
        self.password_input.pack(anchor="center")
        # сообщение
        self.message = ttk.Label(self)
        self.message.pack(anchor="center")

        # определение кнопки
        self.button = ttk.Button(self, text="Войти")
        self.button["command"] = self.button_clicked
        self.button.pack(anchor="center", expand=1)

        self.count_error = {}
        self.count = 0

    def button_clicked(self):
        # Добавить метод авторизация
        # Если метод вернёт True - сообщение
        # Если метод вернёт False - сообщение
        self.log = self.login_input.get()
        self.pas = self.password_input.get()
        print(self.count_error)

        if self.log == '' or self.pas == '':
            self.message['text'] = 'Введите логин или пароль'

        elif UserController.auth(self.log,self.pas) != False:
            # изменить текст у сообщения
            user = UserController.auth(self.log,self.pas)
            print(user.ban)

            # Условие кода счётчик ошибок больше 3
            if user.ban:

                # Блокировать пользователя
                self.message['text'] = "Вы заблокированы. Обратитесь к администратору"
            elif UserController.first(user.id):
                # перейти в окно смены пароля
                window = NewPassword(user)
            else:
                self.message['text'] = 'Вы успешно авторизовались'
                if user.login == 'admin':
                    admin = AdminView()
                # Обнулить счётчик ошибок
                self.count_error = {}
                self.count = 0
        elif UserController.show_login(self.log) is not None:
            # Если такой логин есть в таблице, но парполь не верный
            self.count +=1

            self.count_error = {'login':UserController.show_login(self.log).login, 'count': self.count }
            if self.count_error['count'] >=3:
                UserController.update_all(UserController.show_login(self.log).id, ban=True)
        else:
            # Включить счётчик ошибок ввода
            self.message['text'] = 'Ввели неверный логин или пароль.\n Пожалуйста проверьте ещё раз введенные данные'





if __name__ == "__main__":
    window = AuthView()
    window.mainloop()