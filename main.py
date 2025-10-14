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
        #when user pass a task name as parameter 
        # it is assumed that the user also pass the list name
        # if the list name is empty , list will be default 
        if args.list !=None: 
            exec=controller.create_Task(args.task,args.list)

        else:  
            exec=controller.create_Task(args.task)
          
        #validating if  task were stored successfully      
        if  exec :  
            print("Task created successfully!")
        else:
            print("An error occurred while creating the task.")
    #when user only introduce a list name 
    elif args.list !=None: 
        list_name=args.list 
        if list_name =="": 
            print("please introduce the  task list name ")
        else:  
            exec=controller.create_List(list_name)

            if exec :  
                print("Task list created sucessfully")
            else:  
                print("an error ocurred")
        

  #  else:  
   #     main_menu()
    
