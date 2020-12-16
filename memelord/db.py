import mysql.connector as mysql
from memelord.config import (
    MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_DATABASE
)

def get_conn():
    db = mysql.connect(
        user=MYSQL_USER, 
        passwd=MYSQL_PASSWORD, 
        host=MYSQL_HOST, 
        database=MYSQL_DATABASE,
        )
    return db