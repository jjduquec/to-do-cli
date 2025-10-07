import sqlite3  

class TaskList:  
    def __init__(self,name="default"):
        self.name=name 

    def get_all_lists(self):
        #load the lists names from db 
        conn=sqlite3.connect('tasks.db')
        cursor=conn.cursor()  
        cursor.execute("SELECT name from task_list")
        rows=cursor.fetchall() 
        lists=[row[0] for row in rows]  
        return lists
       