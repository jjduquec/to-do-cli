import argparse 
from controller import create_Task
parse= argparse.ArgumentParser(prog="TO DO cli") 
parse.add_argument("-task","-t",help="name of the task to be added ")
parse.add_argument("-list","-l",help="name of the task list to be created or to add a task")



if __name__=='__main__': 
    #getting the parameters  
    args=parse.parse_args() 
    if args.task and  args.list:  
        #when a task and a list were passed  
        create_Task(args.task,args.list)

    elif args.task:  
        #task is added to a default list  
        create_Task(args.task)
    elif args.list: 
        print("list will be created")
    else:  
        print("execute interface")
