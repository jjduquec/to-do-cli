from prompt_toolkit.shortcuts import choice
from prompt_toolkit import *
from prompt_toolkit import print_formatted_text as print
from controller import Controller
from os import system

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
    lists=controller.get_AllListsName()
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


def get_lists_and_tasks():
    system('cls')  
    controller=Controller() 
    lists=controller.get_AllListsName()  
    options=[(list_name,list_name) for list_name in lists ] 
    options.append(('exit','exit'))
    option=choice(
        message="Select the task list that you want visualize",
        options=options
    )
    system('cls')
    if option != 'exit': 
        #get the tasks by list id 
        tasks=controller.get_TasksByList(option) 
        if len(tasks) > 0 : 
            for task in tasks:  
                print(task[1]) 
        else:  
            print("there are not any task associated to the list") 
        
        system('pause')
    
def delete_list(): 
    system('cls')           
    controller=Controller()  
    task_lists=controller.get_AllLists()
    #-----------list id , list name -------#  
    options=[(task_list[0],task_list[1]) for task_list in task_lists ] 
    options.append(('exit','exit'))
    option=choice(
        message="Select the list that you want delete",
        options=options
    )
    system('cls')
    if option!='exit':
        list_name=controller.get_ListNameById(option)
        if controller.delete_ListById(option):
            print(f"The task list '{list_name}' and his tasks has been deleted succesfully")
        else:  
            print("An error has ocurred while the task list was deleting")
        
        system('pause')

def delete_task():
    system('cls')
    controller=Controller()
    lists=controller.get_AllListsName() 
    
    options=[(task_list,task_list) for task_list in lists ] 
    options.append(('exit','exit'))
    option=choice(
        message="Select the list that contains the task that you want delete",
        options=options
    ) 
    if option!='exit': 
        system('cls')
        tasks=controller.get_TasksByList(option) 
        if len(tasks) > 0 :
            #load tasks associated to the list
            #----------- task id , task name -------# 
            task_options=[(task[0],task[1]) for task in tasks ] 
            task_options.append(('exit','exit'))
            task_option=''
            while task_option != 'exit':
                #indent
                system('cls')
                task_option=choice(
                    message="Select the task that you want delete",
                    options=task_options
                ) 
                if task_option!='exit': 
                    print(task_option)
                    if controller.delete_TaskById(task_option):
                        
                        print("The task has been deleted succesfully")
                    else:  
                        print("An error has ocurred while the task was deleting")
                    system('pause')
        else:  
            print("There are not any task associated to the list")
            system('pause')
       

def main_menu():  
    
    execute=True
    while execute:
        system('cls')
        operation=choice(
            message="Select an operation",
            options=[
                ("new_task","create a new task"),
                ("new_list","create a task list"),
                ("see_lists_and_tasks","see a list and his tasks"),
                ("delete_task","delete a task"), 
                ("delete_list","delete a task list and his tasks"),
                ("exit","exit")
            ]
        )
        if operation=='new_list':
            create_list()
        elif operation=='new_task':
            create_task()
        elif operation=='see_lists_and_tasks':
            get_lists_and_tasks()
        elif operation=='delete_list':
            delete_list()
        elif operation=='delete_task':
            delete_task()
        elif operation=="exit":
            execute=False

