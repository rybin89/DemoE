from tkinter import *
from tkinter import ttk

from Controllers.UserController import UserController
from Views.EditView import EditView


class AdminView(Tk):
    def __init__(self):
        super().__init__()
        # конфигурация окна
        self.title("Админитсратор системы Отеля")
        self.geometry("800x500")
        # Раздел регитсрация пользователя
        self.reg_frame = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[8, 10])
        self.reg_frame.pack(anchor="center", fill =X, padx = 10, pady = 10)
        self.reg_title = ttk.Label(self.reg_frame, text='Регистрация нового пользователя')
        self.reg_title.pack()
        # Логин
        self.login = ttk.Label(self.reg_frame, text="Введите Логин")
        self.login.pack(anchor="center")
        # окно ввода логина
        self.login_input = ttk.Entry(self.reg_frame)
        self.login_input.pack(anchor="center")
        # Пароль
        self.password = ttk.Label(self.reg_frame, text="Пароль")
        self.password.pack(anchor="center")
        # окно ввода ПаролЯ
        self.password_input = ttk.Entry(self.reg_frame, show='*')
        self.password_input.pack(anchor="center")
        # сообщение
        self.message = ttk.Label(self.reg_frame)
        self.message.pack(anchor="center")

        # определение кнопки
        self.button = ttk.Button(self.reg_frame, text="Создать")
        self.button["command"] = self.button_clicked
        self.button.pack(anchor="center", expand=1)

        self.count_error = {}
        self.count = 0

        ########################################################3
        #Таблица
        # определяем столбцы
        columns = ("login", "fullname", "ban")
        self.tree = ttk.Treeview(self, columns=columns, show="headings")
        self.tree.pack(fill=BOTH, expand=1)

        self.table()
        self.tree.bind("<<TreeviewSelect>>",self.item_selected)

        # определение кнопки
        self.button = ttk.Button(self, text="Обновить таблицу")
        self.button["command"] = self.table
        self.button.pack(anchor="center", expand=1)

    def table(self):

        #Очистить таблицу
        for item in self.tree.get_children():
            self.tree.delete(item)
        users = UserController.get() # список пользователей (объект)
        list_users = [] # список кортжей с инф-ей о пользователях
        for user in users:
            if user.ban:
                ban = "Заблокирован"
            else:
                ban = "Разблокирован"
            list_users.append(
                (user.login, user.fullname,ban)
            )

        # определяем заголовки
        self.tree.heading("login", text="Логин")
        self.tree.heading("fullname", text="Имя")
        self.tree.heading("ban", text="Заблокирован")
        # добавляем данные
        for person in list_users:
            self.tree.insert("", END, values=person)

    def item_selected(self,event):
        self.item = self.tree.selection()[0] # Получить строку
        self.user_data = self.tree.item(self.item, "values")[0] # Получить данные из строки [0] - login
        user = EditView(self.user_data)


    def button_clicked(self):
        # Добавить метод авторизация
        # Если метод вернёт True - сообщение
        # Если метод вернёт False - сообщение
        self.log = self.login_input.get()
        self.pas = self.password_input.get()
        if self.log == '' or self.pas == '':
            self.message['text'] = 'Введите логин или пароль'
        elif  UserController.show_login(self.log) is not None:
            self.message['text'] = 'Пользователь с указанным логином уже существует'
        else:
            UserController.add(self.log,self.log,self.password)
            self.message['text'] = f'Пользователь с логином {self.log} создан'
            self.table()

if __name__ == "__main__":
    w = AdminView()
    w.mainloop()