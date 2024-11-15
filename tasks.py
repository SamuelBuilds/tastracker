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
        funcs.dump(data)
    #update existing task
    def update(self, ID, newContent):
        data = funcs.OPEN()
        print(ID)
        print(newContent)
        data[ID-1]["task"]["content"]=newContent
        with open("task.json", "w") as f:
            json.dump(data, f)
    #list existing tasks.
    def list(self):
        data = funcs.OPEN()
        for i in range(len(data)):
            print(data[i]['task']['content'])

