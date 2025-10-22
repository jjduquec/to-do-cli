import sqlite3 

class Task:  
    def __init__(self): 
        self.Name="" 
        self.ListId=1

    def set_Name(self,name):
         self.Name=name    

    def set_ListId(self,ListId) : 
         self.ListId=ListId
        
    def add_task(self): 
          #indentación
          try:
                               
                conn=sqlite3.connect('tasks.db') 
                c=conn.cursor() 
                c.execute("INSERT INTO task (name,list_id) VALUES (?,?)",(self.Name,self.ListId)) 
                conn.commit() 
                conn.close()
                return True
          except:  
               return False

    def get_byListId(self,id): 
         conn=sqlite3.connect('tasks.db')         
         cursor=conn.cursor() 
         cursor.execute("SELECT name FROM task WHERE list_id = ? ",(id,))
         result=cursor.fetchall()  
         return result
          

    

    def __str__(self):  
        if self.task_list=="Default":  
            return self.Name
        else:
            return self.Name + '    ' + self.ListId