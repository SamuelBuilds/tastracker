import json, time

import funcs  
class Task:           
    #add new task
    def add(self, task):
        data = {
            "task":{
                    "content": task,
                    "id": time.time(),
                    "status":"todo",
                    "createdAt": time.ctime(time.time()),
                    "updatedAt": ""#time.ctime(time.time())
                }
            }
        funcs.dump("task.json",data)
    #update existing task
    def update(self, ID, newContent):
        data = funcs.OPEN("task.json")
        oldData = data[ID-1]["task"]["content"]
        print(f"changed:'{oldData}'")
        data[ID-1]["task"]["content"]=newContent  
        data[ID-1]["task"]["updatedAt"]=time.ctime(time.time())     
        with open("task.json", "w") as f:
            json.dump(data, f, indent=3)
        print(f"Update:'{newContent}'")
    #list existing tasks.
    def list(self,status):
        data = funcs.OPEN("task.json")
        for i in range(len(data)):
            if status == "all":
                print(f"{data[i]['task']['content']} | {data[i]['task']['createdAt']} | {data[i]['task']['status']}")
            elif status == "todo":
                if data[i]['task']['status'] == status:
                    print(f"{data[i]['task']['content']} | {data[i]['task']['createdAt']} | {data[i]['task']['status']}")
                else:
                    continue
            elif status == "in-progress":
                if data[i]['task']['status'] == status:
                    print(f"{data[i]['task']['content']} | {data[i]['task']['createdAt']} | {data[i]['task']['status']}")
                else:
                    continue
            elif status == "done":
                if data[i]['task']['status'] == status:
                    print(f"{data[i]['task']['content']} | {data[i]['task']['createdAt']} | {data[i]['task']['status']}")
                else:
                    continue
            else:
                print("Please provided a valid request.\n In the scope of:\nall\ntodo\nin-progress\ndone")
                
    #pop task
    def delete(self, ID):
        data=funcs.OPEN("task.json")
        try:
            data.pop(ID-1)
            funcs.wdump("task.json",data)
        except IndexError:
            print("The tasks your trying to delete doesn't exist.")
    #give a task the status of done
    def mark_done(self, ID):
        data = funcs.OPEN("task.json")
        data[ID-1]["task"]["status"]="done"
        funcs.wdump("task.json",data)
    #give a task the status in-progress
    def mark_in_progress(self, ID):
            data = funcs.OPEN("task.json")
            data[ID-1]["task"]["status"]="in-progress"
            funcs.wdump("task.json",data)