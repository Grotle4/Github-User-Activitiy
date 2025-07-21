import requests
import json

username = input("Please enter a username: ").lower()
url = f"https://api.github.com/users/{username}/events"
r = requests.get(url)
events = r.json()


def search_for_values(r, events):
    try:
        if events:
            event_name_list = []
            event_type_list = []
            for event in events: #getting values from JSON output
                event_name = event["repo"]["name"]
                event_type = event["type"]
                event_name_list.append(event_name)
                event_type_list.append(event_type)
            name_set = set(event_name_list)
            type_set = set(event_type_list)
            
            return name_set, type_set
        else:
            print("No Events found.")
    except:
        pass

name_set, type_set = search_for_values(r,events)
print(type_set)
print(name_set)