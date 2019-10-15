import pyodbc
import sys
def fn(x,id,pref1,pref2):
    sql='insert into party1 values({},\'{}\',\'{}\',\'{}\');'.format(id,x,pref1,pref2)
    try:
        conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=server_name;'
                      'Database=db_name;'
                      'Trusted_Connection=yes;')
        conn.execute('pragma journal_mode=wal')
        print(sql)
        cur1=conn.cursor()
        cur1.execute(sql)
        conn.commit()
        return "Thank you"
    except:
        print('Error',sys.exc_info()[0])
        return "Error"
 
