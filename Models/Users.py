from datetime import datetime

from Connection.connect import *
from Models.Roles import Roles


class Users(Model):
    id = PrimaryKeyField()
    login = CharField(unique=True,max_length=150)
    password = CharField()
    ban = BooleanField(default=False)
    first_auth = BooleanField(default=True)
    created = DateTimeField(default=datetime.now())
    last_auth = DateTimeField(default=None)
    fullname = CharField()
    role_id = ForeignKeyField(Roles)


    class Meta:
        database = mysql_db # this model uses the "people.db" database