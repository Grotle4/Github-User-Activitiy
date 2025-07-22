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

    for check in event_name_check:
        new_dict = {}
        
        new_dict = {check:{"id": 0, "task" :"N/A" , "amount": 0}}
        dict_ammount = 0 
        print("dict name", new_dict)
        for event in event_dict:
            name = event_dict[event]["name"]
            if name == check:
                for type_check in event_type_check:
                    type = event_dict[event]["type"]
                    print(type)
                    if type == type_check:
                        print("this is my type: ", type)
                        if type not in new_dict[check]["task"]:
                            new_dict[check]= []
                            new_dict[check].append({"task": type}, "amount: 0"})
                            new_dict[check]["amount"] += 1
                        else:
                            pass
                        
        list_of_dicts.append(new_dict)

                        
                        
        
    print(list_of_dicts)
    return list_of_dicts





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
"""     for check in event_name_check:
        print("iteration loop")
        for index, event in enumerate(event_dict):
            check_name = event_dict[index]["name"]
            if check == check_name:
                print("name correct")
                stored_dict[check_name] = {}
                print("1:", stored_dict)
                for type_check in event_type_check:
                    iteration = 0
                    print("type_check: ",type_check)
                    type_name = event_dict[index]["type"]
                    print("event_type: ", type_name)
                    if type_check == event_dict[index]["type"]:
                        iteration += 1
                        stored_dict[check_name][type_check] = iteration
                        print("2: ", stored_dict) """
                
        

event_dict, event_name_check, event_type_check = search_for_values(r,events)
final_output = output_sets(event_dict, event_name_check, event_type_check)
print("final: ", final_output)


