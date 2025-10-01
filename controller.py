from task import Task 

task_lists=["Default"]
tasks=[]
def create_Task(task,task_list="Default"): 
    new_task= Task(task,task_list)
    tasks.append(new_task)
    print("Task created!")

