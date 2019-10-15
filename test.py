import sqlite3
import sys
def fn(x,id,pref1,pref2):
    sql='insert into party1 values({},\'{}\',\'{}\',\'{}\');'.format(id,x,pref1,pref2)
    try:
        with sqlite3.connect('SSI_Data.db', isolation_level=None) as conn:
            print("Opened database successfully")
            conn.execute('pragma journal_mode=wal')
            print(sql)
            cur1=conn.cursor()
            cur1.execute(sql)
            conn.commit()
        return "Thank you"
    except:
        print('Error',sys.exc_info()[0])
        return "Error"
