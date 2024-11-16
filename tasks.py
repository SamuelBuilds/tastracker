import json, time
import funcs  
class Task:           
    #add new task
    def add(self, task):
        data = {
            "task":{
                    "content": task,
                    "id": time.time()
                }
            }
        funcs.dump("task.json",data)
    #update existing task
    def update(self, ID, newContent):
        data = funcs.OPEN("task.json")
        oldData = data[ID-1]["task"]["content"]
        print(f"changed:'{oldData}'")
        data[ID-1]["task"]["content"]=newContent       
        with open("task.json", "w") as f:
            json.dump(data, f, indent=3)
        print(f"Update:'{newContent}'")
    #list existing tasks.
    def list(self):
        data = funcs.OPEN("task.json")
        for i in range(len(data)):
            print(data[i]['task']['content'])
    #pop task
    def delete(self, ID):
        data=funcs.OPEN("task.json")
        try:
            data.pop(ID-1)
            funcs.wdump("task.json",data)
        except IndexError:
            print("The tasks your trying to delete doesn't exist.")

