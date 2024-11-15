import json, time

def OPEN():
    with open("task.json", 'r') as file:
        data = json.load(file)
        return data
def dump(d):
    try:
        data = OPEN()
        if isinstance(data, list):
            data.append(d) 
        else:
            data = [data, d] 
            with open("task.json", 'w') as file:
                json.dump(d, file, indent=4)
    except json.JSONDecodeError:
        with open("task.json", 'w') as file:
            json.dump(d, file, indent=4)
    except FileNotFoundError:
        print("Error: The file does not exist.")
   
class Task:           
    def add(self, task):
        data = {
            "task":{
                    "content": task,
                    "id": time.time()
                }
            }
        dump(data)
    def update(self, ID, newContent):
        data = OPEN()
        print(ID)
        print(newContent)
        data[ID-1]["task"]["content"]=newContent
        with open("task.json", "w") as f:
            json.dump(data, f)


