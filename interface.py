from prompt_toolkit.shortcuts import choice
from prompt_toolkit import print_formatted_text as print
from prompt_toolkit import prompt 
from controller import Controller
from os import system

def main_menu():  
    
    execute=True
    while execute:
        system('cls')
        operation=choice(
            message="Select an operation",
            options=[
                ("new_task","create a new task"),
                ("delete_task","delete a task"), 
                ("new_list","create a task list"),
                ("delete_list","delete a task list"),
                ("exit","exit")
            ]
        )
        if operation=='new_list':
            create_list()
        elif operation=='new_task':
            create_task()
        elif operation=="exit":
            execute=False

def create_list (): 
    system('cls')
    list_name = prompt('Introduce the name of the new task list \n')
    if list_name=="": 
        print("Error, task list name can not be empty\n")
        
       
    else:  
        controller=Controller()  
        if controller.create_List(list_name): 
            print("Task list has been created succesfully \n")
           
        else:  
            print("An error ocurred while task list was creating\n")
    
    system('pause')

def create_task():  
    system('cls')
    controller=Controller()
    lists=controller.get_AllLists()
    task_name=prompt("Introduce the name of the task \n")
    task_list=choice(
        message="Select the task list to associate the task",
        options=[(list_name,list_name) for list_name in lists ]
    )
    if task_name=="":
        print("Error, task name can not be empty")
    else:
        if controller.create_Task(task_name,task_list):
            print("Task was created sucessfully")
        else:
            print("An error has ocurred while task was creating")

    system('pause')
    
