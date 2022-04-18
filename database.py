import pymysql as mq   # 1 import pymysql

my_obj = mq.connect(host="localhost", user="root", password="")  # crate connection with database

cursor_obj = my_obj.cursor()  # 3 create object of cursor

# start use of try and except
try:
    db = "create database school"
    cursor_obj.execute(db)
    print("school database created")
    # cursor_obj.execute(query_create_table)
    # print("school database created")

except:
    print("create database error")