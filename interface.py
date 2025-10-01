from prompt_toolkit.shortcuts import choice  


def main_menu():  
    operation=choice(
        message="Select an operation",
        options=[
            ("new_task","create a new task"),
            ("delete_task","delete a task"), 
            ("new_list","create a task list"),
            ("delete_list","delete a task list")
        ]
    )
    print(f"the operation selected is {operation}")