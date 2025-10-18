from models.task import Task 
from models.list import TaskList

class Controller():  

    def __init__(self): 
        pass

    def create_Task(self,task,list_name="default"): 
        task_list=TaskList(list_name)
        list_id=0 
        while list_id==0: 
            list_id=task_list.get_id()  
            if list_id == 0:  
                task_list.add_list() 
        new_task= Task(task,list_id)  
        return new_task.add_task()

        
    def create_List(self,list_name):  
        task_list=TaskList(list_name)
        return task_list.add_list()   


    def get_AllLists(self): 
        task_list=TaskList()  
        return task_list.get_all_lists()


