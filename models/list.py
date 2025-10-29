import sqlite3  

class TaskList:  
    def __init__(self):
        self.name="default" 
        self.id=0

    def set_Id(self,id): 
        self.id=id

    def set_Name(self,name): 
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


    def get_AllListsName(self):
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
    
    def get_AllLists(self):
        #load the lists names from db 
        try:
            conn=sqlite3.connect('tasks.db')
            cursor=conn.cursor()  
            cursor.execute("SELECT * from task_list")
            rows=cursor.fetchall() 
            return [(row[0],row[1]) for row in rows]
        except:  
            return []       


    def get_Id(self): 
        try:
            conn=sqlite3.connect('tasks.db')
            cursor=conn.cursor()  
            cursor.execute(f"SELECT list_id from task_list WHERE name = ?",(self.name,))
            rows=cursor.fetchall()  
            if len(rows)==0: 
                return 0  
            else:  
               return rows[0][0]
        except:  
            return 0
        
    def get_NameById(self): 
        try:
            conn=sqlite3.connect('tasks.db')
            cursor=conn.cursor()  
            cursor.execute(f"SELECT name from task_list WHERE list_id = ?",(self.id,))
            rows=cursor.fetchall()  
            if len(rows)==0: 
                return ""  
            else:  
                return rows[0][0]
        except:  
            return ""   

    def delete_ById(self,id):
        try:
            conn=sqlite3.connect('tasks.db')
            cursor=conn.cursor()
            cursor.execute("DELETE FROM task_list WHERE list_id= ?",(id,))
            conn.commit()
            conn.close()
            return True  
        except: 
             return False
