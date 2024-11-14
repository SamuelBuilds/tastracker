import argparse, json, time

parser = argparse.ArgumentParser()
parser.add_argument("--add", help="Add a new task.")
args = parser.parse_args()

class Task:
    def __init__(self, task):
        self.task = task
        self.id = time.time()
        self.data = {
            "task":{
                    "content":self.task,
                    "id": self.id
                }
            }
    
    def dump(self):
            try:
                with open("task.json", 'r') as file:
                    data = json.load(file)

                if isinstance(data, list):
                    data.append(self.data) 
                else:
                    data = [data, self.data] 

                
                with open("task.json", 'w') as file:
                    json.dump(data, file, indent=4)
            except json.JSONDecodeError:
                with open("task.json", 'w') as file:
                    json.dump(self.data, file, indent=4)
            except FileNotFoundError:
                print("Error: The file does not exist.")
    
    def read(self):
        with open("task.json","r") as f:
            data = json.load(f)
        return data

task = Task(args.add)
task.dump()
read = task.read()
print(len(read))