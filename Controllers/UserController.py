
from Models.Users import Users


class UserController:
    # вывод польщователя по логину
    @classmethod
    def show_login(cls, login):
        return Users.get_or_none(Users.login==login)

    # Метод авторизации пользователя
    """
    Пользователь вводит логин и пароль
    Если пользователь есть в таблице,
    то проверяется соответсвие введённого пароля с паролем в Таблице,
    если соответсвут метод возвращает True,
    иначе возвращает False
    """

    # def auth(self, login, password):
    #     user = Users.get_or_none(Users.login==login)
    #     if user is not None:
    #         if user.password == password:
    #             return {
    #                 'message':True,
    #                 'user':user
    #                     }
    #         else:
    #             return {'message':False}
    #     else:
    #         return {'message':False}
    @classmethod
    def auth(cls, login, password):
        user = Users.get_or_none(Users.login==login)
        if user is not None:
            if user.password == password:
                return user

            else:
                return False
        else:
            return False

    @classmethod
    def update(cls,user_id,old_password,new_password):
        """
        Метод обновления пароля
        :param user_id:id пользователя
        :param old_password:Старый пароль
        :param new_password:Новый пароль
        :return:
        """

        user = Users.get_by_id(user_id)

        if user.password == old_password:

            Users.update({
                Users.password:new_password,
                Users.first_auth:False,
            }).where(Users.id == user_id).execute()
            return True
        else:

            return False

    @classmethod
    def first(cls,user_id):
        """
        Возвращает True если пользователь первый раз авторизуется
        :param user_id:id пользователя
        :return:
        """
        user = Users.get_by_id(user_id)
        print(user.first_auth)
        if user.first_auth == True:
            return True
        else:
            return False
    # Универсальный метод обновления
    @classmethod
    def update_all(cls,id,**fields):
        for key, value in fields.items():
            Users.update({key:value}).where(Users.id == id).execute()
    ##########################################################
    ##########################################################
    ##########################################################
    @classmethod
    def add(cls, login,fullname, password):
        Users.create(
            login=login,
            fullname=fullname,
            password =password,
            role_id = 2
        )


if __name__ == "__main__":
    # UserController.update(1,'admin','admin1')
    # UserController.update_all(2,fullname = 'User1212', password = '1111111')
    print(UserController.show_login('admin1'))
    UserController.add('user2','user2','user2')


