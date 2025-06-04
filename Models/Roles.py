from Connection.connect import *

class Roles(Model):
    id = PrimaryKeyField()
    name = CharField(unique=True, max_length=100)



    class Meta:
        database = mysql_db # this model uses the "people.db" database