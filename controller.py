from models.task import Task 
from models.list import TaskList

class Controller():  

    def __init__(self): 
        pass

    def create_Task(self,task,list_name="default"): 
        task_list=TaskList(list_name)
        list_id=task_list.get_id()
        if list_id == 0 :
            return False 
        else:  
            new_task= Task(task,list_id)  
            return new_task.add_task()

        
       

