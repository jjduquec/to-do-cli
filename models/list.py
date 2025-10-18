import sqlite3  

class TaskList:  
    def __init__(self,name="default"):
        self.name=name 
        

    def add_list(self):
        try:
            conn=sqlite3.connect("tasks.db")
            cursor=conn.cursor() 
            cursor.execute("INSERT INTO task_list (name) VALUES(?)",(self.name,))
            conn.commit()
            conn.close()
            return True  
        except:  
            return False


    def get_all_lists(self):
        #load the lists names from db 
        try:
            conn=sqlite3.connect('tasks.db')
            cursor=conn.cursor()  
            cursor.execute("SELECT * from task_list")
            rows=cursor.fetchall() 
            lists=[row[1] for row in rows]
              
            return lists
        except:  
            return [] 
        
        


    def get_id(self): 
        conn=sqlite3.connect('tasks.db')
        cursor=conn.cursor()  
        cursor.execute(f"SELECT list_id from task_list WHERE name = ?",(self.name,))
        rows=cursor.fetchall()  
        if len(rows)==0: 
            return 0  
        else:  
           return rows[0][0]
       

