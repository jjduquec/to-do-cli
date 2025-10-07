import sqlite3 

class Task:  
    def __init__(self,name,task_list=1): 
        self.name=name 
        self.task_list=task_list  
        
    def add_task(self): 
          #indentación
          try:
                
                conn=sqlite3.connect('tasks.db') 
                c=conn.cursor() 
                c.execute("INSERT INTO task (name,list_id) VALUES (?,?)",(self.name,self.task_list)) 
                conn.commit() 
                conn.close()
                return True
          except:  
               return False
                
          

    

    def __str__(self):  
        if self.task_list=="Default":  
            return self.name
        else:
            return self.name + '    ' + self.task_list