import argparse 
#from interface import main_menu
from controller import Controller

parse= argparse.ArgumentParser(prog="TO DO cli") 
parse.add_argument("-task","-t",help="name of the task to be added ")
parse.add_argument("-list","-l",help="name of the task list to be created or to add a task")



if __name__=='__main__': 
    #getting the parameters  
    args=parse.parse_args() 
    controller=Controller()
    

    if args.task != None :  
        #when a task and a list were passed  
        if args.list !=None: 
            exec=controller.create_Task(args.task,args.list)
        else:  
            exec=controller.create_Task(args.task)
          
            
        if  exec :  
            print("Task created successfully!")
        else:
            print("An error occurred while creating the task.")

    elif args.list !=None: 
        print("list will be created")
  #  else:  
   #     main_menu()
    
