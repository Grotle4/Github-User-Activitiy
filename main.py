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
    list_of_dicts = []

    for check in event_name_check: #runs through all task names collected
        iteration = 0 #sets iteration to 0 on loop through
        for type in event_type_check: #runs through all event types collected
            for event in event_dict: #runs through every event in dictionary
                name_val = event_dict[event]["name"]  
                type_val =  event_dict[event]["type"]
                if check == name_val and type == type_val: #if name and type match up
                    iteration += 1
                    stored_dict["name"] = check
                    stored_dict["type"] = type #set all values and make a copy
                    stored_dict["amount"] = iteration
                    finished_dict = stored_dict.copy()            
            else:
                iteration = 0 #resets iteration to 0 for next values
                list_of_dicts.append(finished_dict) #when loop is finish, append copy of list to final list of dictionaries
    return list_of_dicts    


        

event_dict, event_name_check, event_type_check = search_for_values(r,events)
final_output = output_sets(event_dict, event_name_check, event_type_check)
print("final: ", final_output) #take this final output value and output it as print statements in a function


