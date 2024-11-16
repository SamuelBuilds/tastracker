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
#list by status
List.add_argument("status", nargs="?", default=None, type=str, help="specify status i.e todo, in-progress, done")
#delete
delete = subparsers.add_parser("delete", help="Delete specific task")
delete.add_argument("deleteID", type = int, help="specific task ID for deletion")
#mark-done
mark_done = subparsers.add_parser("mark-done", help="Mark done specific task.")
mark_done.add_argument("mdID", type=int, help="specify Id of task to mark as done.")
#mark-in-progress
mark_in_progress = subparsers.add_parser("mark-in-progress", help='Mark "in-progress" specific task.')
mark_in_progress.add_argument("ipID",type=int, help="specify Id of task to mark as in-pogress.")
args = parser.parse_args()