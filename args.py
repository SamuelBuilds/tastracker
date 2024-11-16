import argparse

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command", help="subcommands")
#add
add=subparsers.add_parser("add", help="Add a new task.")

add.add_argument("add", help="Add a new task.")
#update 
update=subparsers.add_parser("update", help="update a specific task by ID")
update.add_argument("updateID", type=int, help="Specify task id for updating")
update.add_argument("newContent", type=str,help="add new change")
#list
List = subparsers.add_parser("list", help="list tasks")
#delete
delete = subparsers.add_parser("delete", help="Delete specific task")
delete.add_argument("deleteID", type = int, help="specific task ID for deletion")

args = parser.parse_args()