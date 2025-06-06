from datetime import datetime
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

        # Словарь для подсчёта количество неправильных попыток ввода пароля у Пользователя в БД
        self.count_error = {}


    def button_clicked(self):
        # Добавить метод авторизация
        # Если метод вернёт True - сообщение
        # Если метод вернёт False - сообщение
        self.user_login = self.login_input.get()
        self.user_password = self.password_input.get()


        if self.user_login == '' or self.user_password == '':
            self.message['text'] = 'Введите логин или пароль'

        # переменной user передаём результат выполнения метода auth
        user = UserController.auth(self.user_login,self.user_password)
        if user != False:
            # Условие кода счётчик ошибок больше 3
            # Проверка 30 дней
            if user.last_auth is not None:
                delta_days  = datetime.now() - user.last_auth # Текущая дата и время минус дата и время создания файла
                if delta_days.days >=30: # Сравниваем промежуток времени с 30, .days - переводит дату и время в число дней
                    UserController.update_all(user.id,ban = True)
                    user = UserController.show_login(user.login)
            if user.ban:
                # Блокировать пользователя
                self.message['text'] = "Вы заблокированы. Обратитесь к администратору"
            elif UserController.first(user.id):
                # перейти в окно смены пароля
                window = NewPassword(user)
            else:
                self.message['text'] = 'Вы успешно авторизовались'
                UserController.update_all(user.id,last_auth = datetime.now()) # Изменить дата время авторизации на текущую
                if user.login == 'admin':
                    admin = AdminView()
                # Обнулить счётчик ошибок
                if user.login is self.count_error:
                    del self.count_error[user.login] # del удаляет из словаря self.count_error атрибут и ключ user.login
        if UserController.show_login(self.user_login) is not None: # проверка существования логина в таблице
            # Если такой логин есть в таблице, но парполь не верный
            # Начало почсёта количества неправильных попыток
            if self.user_login not in self.count_error:
                self.count_error[self.user_login] = 0  # добавить в словарь ключ значение self.count_error{логин:0}
            self.count_error[self.user_login] +=1 # увеличиваем заначения ключа на 1 self.count_error{логин:0+1}
            # усли занчения ключа словаря >=3
            if self.count_error[self.user_login] >=3:
                UserController.update_all(UserController.show_login(self.user_login).id, ban=True)
        else:
            # Включить счётчик ошибок ввода
            self.message['text'] = 'Ввели неверный логин или пароль.\n Пожалуйста проверьте ещё раз введенные данные'





if __name__ == "__main__":
    window = AuthView()
    window.mainloop()