class Task:  
    def __init__(self,name,task_list="Default"): 
        self.name=name 
        self.task_list=task_list  
        

    def __str__(self):  
        if self.task_list=="Default":  
            return self.name
        else:
            return self.name + '    ' + self.task_list