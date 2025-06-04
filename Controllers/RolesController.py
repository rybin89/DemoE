from Models.Users import *


class RoleController:

    @classmethod
    def add(cls,name):
        Roles.create(name=name)
    @classmethod
    def get(cls):
        return Roles.select()



if __name__ == "__main__":
    pass