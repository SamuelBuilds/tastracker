import argparse, json, time
import tasks as t

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command", help="subcommands")
#add parser
add=subparsers.add_parser("add", help="Add a new task.")

add.add_argument("add", help="Add a new task.")
#update parser
update=subparsers.add_parser("update", help="update a specific task by ID")
update.add_argument("ID", type=int, help="Specify task id")
update.add_argument("newContent", type=str,help="add new change")
args = parser.parse_args()
if args.command=="add":
    task = t.Task()
    task.dump(args.add)
elif args.command=="update":
    task = t.Task()
    task.update(args.ID, args.newContent)
else: 
    print("""
    Welcome to your task tracker!\n 
    Usage:
    Add A New Task:
    task-cli add [new task]
    Update:
    task-cli update [task number] [Your Update]
    """)
