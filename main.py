import requests
import json

username = input("Please enter a username: ").lower()
url = f"https://api.github.com/users/{username}/events"
r = requests.get(url)
events = r.json()


def search_for_values(r, events):
    try:
        if events:
            event_name_check = []
            event_type_check = []
            event_dict = {}
            for index, event in enumerate(events): #getting values from JSON output
                event_dict[index] = {}
                event_name = event["repo"]["name"] #change this to nested dict
                event_type = event["type"]
                event_name_check.append(event_name)
                event_type_check.append(event_type)
                event_dict[index]["name"] = event_name
                event_dict[index]["type"] = event_type
            event_name_check = set(event_name_check)
            event_type_check = set(event_type_check) #make this function if it works
            event_name_check = list(event_name_check)
            event_type_check = list(event_type_check)
            
            return event_dict, event_name_check, event_type_check
        else:
            print("No Events found.")
    except:
        pass

def output_sets(event_dict, event_name_check, event_type_check):
    stored_dict = {}
    internal_dict = {}
    list_of_dicts = []

    for check in event_name_check: #runs through all task names collected
        iteration = 0
        for type in event_type_check:
            for event in event_dict:
                name_val = event_dict[event]["name"]  
                type_val =  event_dict[event]["type"]
                if check == name_val:
                    if type == type_val:
                        iteration += 1
                        stored_dict["name"] = check
                        stored_dict["type"] = type
                        stored_dict["amount"] = iteration
                        print("iteration: ", iteration)
                        finished_dict = stored_dict.copy()            
            else:
                iteration = 0
                list_of_dicts.append(finished_dict)
    print(list_of_dicts)    













                        
                        



"""     for check in event_name_check: #runs through Task_tracker, then number guessing game
        new_dict = {}
        name_list = []
        new_dict = {check:{"amount": 0}}
        dict_ammount = 0 
        previous_type = None
        print("dict name", new_dict)
        for event in event_dict: #runs through all events
            name = event_dict[event]["name"]
            if name == check: #if the name matches the check being looped through
                for type_check in event_type_check: #run through push event then create event
                    type = event_dict[event]["type"]
                    print(type)
                    if type == type_check: #if the type matches up
                        print("this is my type: ", type)
                        if type == previous_type:
                            new_dict[check]["type"] = type
                            new_dict[check]["amount"] += 1
                        elif type != previous_type:
                            pass
                            print("done")
                            list_of_dicts.append(new_dict)
                previous_type = type """


""" print("AHHHHHHH:", event_type_check)
for check in event_name_check:
    print("1: ",stored_dict)
    print("iteration loop")
    for type_check in event_type_check:
        print("2: ",stored_dict)
        iteration = 0
        for index, event in enumerate(event_dict):
            print("3: ",stored_dict)
            type_name = event_dict[index]["type"]
            check_name = event_dict[index]["name"]
            if check == check_name:
                print("name correct")
                print("4: ",stored_dict)
                if type_check == type_name:
                    print("type correct")
                    iteration += 1
                    stored_dict[check_name][type_check] = iteration
                    print("5: ",stored_dict)
"""            
        

event_dict, event_name_check, event_type_check = search_for_values(r,events)
final_output = output_sets(event_dict, event_name_check, event_type_check)
print("final: ", final_output)


