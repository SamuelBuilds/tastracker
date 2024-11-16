import json, time
import tasks as t
from args import *
task = t.Task()
if args.command=="add":
    task.add(args.add)
elif args.command=="update":
    task.update(args.updateID, args.newContent)
elif args.command == "list":
    try:
         task.list()
    except json.JSONDecodeError:
        print("You might not have any task!")
elif args.command == "delete":
    task.delete(args.deleteID)
else: 
    print("""
    Welcome to your task tracker!\n 
    Usage:
    Add a new task:
    task-cli add [new task]
    Update specific task:
    task-cli update [task number] [Your Update]
    List all tasks:
    task-cli list 
    delete specific task:
    task-cli delete [task number]
    """)
