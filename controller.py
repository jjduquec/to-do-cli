from models.task import Task 
from models.list import TaskList

class Controller():  

    def __init__(self): 
        pass

    def create_Task(self,task,list_name="default"): 
        new_task=Task()
        if list_name!="default": 
            #verify if task list it's new or no 
            task_list=TaskList()
            task_list.set_Name(list_name)
            list_id=0 
            while list_id==0: 
                list_id=task_list.get_id()  
                if list_id == 0:  
                    task_list.add_list() 
            new_task.set_ListId(list_id)
      
        new_task.set_Name(task)
        
        return new_task.add_task()

        
    def create_List(self,list_name):  
        task_list=TaskList()
        task_list.set_Name(list_name)
        return task_list.add_list()   


    def get_AllLists(self): 
        task_list=TaskList()  
        return task_list.get_all_lists()

    def get_TasksByList(self,list_name): 
        task_list=TaskList() 
        task_list.set_Name(list_name)
        id=task_list.get_id()  
        task=Task() 
        tasks=task.get_AllByListId(id) 
        return tasks
        


