class Task:  
    def __init__(self,name,task_list=None): 
        self.name=name 
        self.task_list=task_list  
        

    def __str__(self):  
        if self.task_list==None:  
            return self.name
        else:
            return self.name + '    ' + self.task_list