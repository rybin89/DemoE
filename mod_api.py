import json
import re
from tkinter import *
from tkinter import ttk

from requests import get


class ModApi(Tk):
    def __init__(self):
        super().__init__()
        self.api_url = 'http://prb.sylas.ru/TransferSimulator/fullName'
        # получить api
        # конфигурация окна
        self.title("Валидация данных")
        self.geometry("500x250")
        self.data_api = ttk.Frame(self)
        self.data_api.pack(anchor="center", fill = X, padx = 10, pady = 10)
        self.data_button = ttk.Button(self.data_api,text='Получить данные',command=self.get_fullname)
        self.data_button.grid(sticky=NSEW, row = 0, column =0, ipadx=50, ipady=6, padx=4, pady=4)
        self.data_fullname = ttk.Label(self.data_api, text='Text')
        self.data_fullname.grid(sticky=E,row = 0, column =1, ipadx=6, ipady=6, padx=4, pady=4)

        # Валидация
        self.validate = ttk.Frame(self)
        self.validate.pack(anchor="center", fill = X, padx = 10, pady = 10)
        self.validate_button = ttk.Button(self.validate, text='Отправить результат теста',command=lambda: self.validate_fullname_button(self.fullname) )
        self.validate_button.grid(sticky=NSEW, row=0, column=0, ipadx=50, ipady=6, padx=4, pady=4)
        self.validate_fullname = ttk.Label(self.validate)
        self.validate_fullname.grid(sticky=E, row=0, column=1, ipadx=6, ipady=6, padx=4, pady=4)
        self.fullname = ''
    def get_fullname(self):
        response = get(self.api_url,{'key':'value'})
        # response.json() - метод json() преобразует json в словарь
        print(response.json())
        fullname = response.json()['value']
        self.data_fullname['text'] = fullname
        self.fullname = fullname



    def validate_fullname_button(self, fullname):
        # Проверка на допусимые символы
        #переменная для регулярного вырожения
        pattern = r'^[а-яА-ЯёЁ]+\s[а-яА-ЯёЁ]+\s[а-яА-ЯёЁ]+$'
        if re.fullmatch(pattern,fullname):
            self.validate_fullname['text'] = 'Валидация прошла успешно'
            return True
        else:
            self.validate_fullname['text'] = 'ФИО содержит запрещённые символы'
            return False

if __name__ == "__main__":
    window = ModApi()
    window.mainloop()


