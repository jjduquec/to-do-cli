import argparse 

parse= argparse.ArgumentParser(prog="TO DO cli") 
parse.add_argument("-task","-t",help="name of the task to be added ")
parse.add_argument("-list","-l",help="name of the task list to be created or to add a task")



if __name__=='__main__': 
    #getting the parameters  
    args=parse.parse_args() 
    if args.task and  args.list:  
        print("parameters received")
    elif args.task:  
        #task is added to a default list  
        print("task will be added to default list")
    elif args.list: 
        print("list will be created")
    else:  
        print("execute interface")
