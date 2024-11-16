import json

#open file for reading
def OPEN(filepath: str):
    with open(filepath, 'r') as file:
        data = json.load(file)
        return data
    
#dump to file #1
def dump(filepath: str,d):
    try:
        data = OPEN("task.json")
        if isinstance(data, list):
            data.append(d) 
        else:
            data = [data, d] 
        with open(filepath, 'w') as file:
            json.dump(data, file, indent=3)
    except json.JSONDecodeError:
        with open(filepath, 'w') as file:
            json.dump([d], file, indent=3)
    except FileNotFoundError:
        print("Error: The file does not exist.")

#dump to file #2
def wdump(filepath: str,data):
    with open(filepath, "w") as f:
        json.dump(data, f, indent=3)