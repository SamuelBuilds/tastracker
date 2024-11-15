import argparse, json, time
import tasks as t

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command", help="subcommands")
#add
add=subparsers.add_parser("add", help="Add a new task.")

add.add_argument("add", help="Add a new task.")
#update 
update=subparsers.add_parser("update", help="update a specific task by ID")
update.add_argument("ID", type=int, help="Specify task id")
update.add_argument("newContent", type=str,help="add new change")
#list
List = subparsers.add_parser("list", help="list tasks")
args = parser.parse_args()
task = t.Task()
if args.command=="add":
    task.add(args.add)
elif args.command=="update":
    task.update(args.ID, args.newContent)
elif args.command == "list":
    try:
         task.list()
    except json.JSONDecodeError:
        print("You might not have any task!")
else: 
    print("""
    Welcome to your task tracker!\n 
    Usage:
    Add A New Task:
    task-cli add [new task]
    Update:
    task-cli update [task number] [Your Update]
    """)
