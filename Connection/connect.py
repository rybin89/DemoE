from peewee import *

# Connect to a MySQL database on network.
mysql_db = MySQLDatabase('rybin_demo1',
                         user='rybin_demo2',
                         password='111111',
                         host='10.11.13.118',
                         port=3306
                         )

if __name__ == "__main__":
    mysql_db.connect()