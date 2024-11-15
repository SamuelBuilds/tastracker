import json
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
            json.dump(data, file, indent=3)
    except json.JSONDecodeError:
        with open("task.json", 'w') as file:
            json.dump([d], file, indent=3)
    except FileNotFoundError:
        print("Error: The file does not exist.")
 