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

    def get_AllByListId(self,id): 
         
         conn=sqlite3.connect('tasks.db')         
         cursor=conn.cursor() 
         cursor.execute("SELECT task_id,name FROM task WHERE list_id = ? ",(id,))
         rows=cursor.fetchall()  
        
         if len(rows) > 0 : 
                return rows 
         else:  
              return []

    def delete_ById(self,id):
        try:
            conn=sqlite3.connect('tasks.db')
            cursor=conn.cursor()
            cursor.execute("DELETE FROM task WHERE task_id= ?",(id,))
            conn.commit()
            conn.close()
            return True  
        except: 
             return False 
        
    def delete_ByListId(self,id):
        try:
            conn=sqlite3.connect('tasks.db')
            cursor=conn.cursor()
            cursor.execute("DELETE FROM task WHERE list_id= ?",(id,))
            conn.commit()
            conn.close()
            return True  
        except: 
             return False 
            
        
        
         
         
         
          

    

    def __str__(self):  
        if self.task_list=="Default":  
            return self.Name
        else:
            return self.Name + '    ' + self.ListId