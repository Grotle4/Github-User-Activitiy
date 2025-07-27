import requests
import argparse



def search_for_values(r, events):
    try:
        if events:
            event_name_check = []
            event_type_check = []
            event_dict = {}
            for index, event in enumerate(events): #getting values from JSON output
                event_dict[index] = {}
                event_name = event["repo"]["name"]
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

def give_output(final_output,filtering_types,filtered_types):
    print("Output:")
    for event in final_output: #Do this for each event taken
            if filtering_types == True:
                for filtered in filtered_types:
                    if event["type"].lower() == filtered.lower():
                        print("working")
                        output_message(event)
            else:
                output_message(event)
                


def output_message(event):
    match event["type"]:
                case "CommitCommentEvent":
                    print(f"Created {event["amount"]} {check_plural(event, "comment")} on {event["name"]}")
                case "CreateEvent":
                    print(f"Created {event["amount"]} {check_plural(event, "branch")} on {event["name"]}")
                case "DeleteEvent":
                    print(f"Deleted {event["amount"]} {check_plural(event, "branch")} on {event["name"]}")
                case "ForkEvent":
                    print(f"Forked {event["amount"]} {check_plural(event, "time")} on {event["name"]}")
                case "GollumEvent":
                    print(f"Created or Updated wiki page {event["amount"]} {check_plural(event, "time")} on {event["name"]}")
                case "IssueCommentEvent":
                    print(f"Had activity {event["amount"]} {check_plural(event, "time")} on {event["name"]}")
                case "IssuesEvent":
                    print(f"Had an issue {event["amount"]} {check_plural(event, "time")} on {event["name"]}")
                case "MemberEvent":
                    print(f"Had an activity with collaborators {event["amount"]} {check_plural(event, "time")} on {event["name"]}")
                case "PublicEvent":
                    print(f"Made repository public {event["amount"]} {check_plural(event, "time")} on {event["name"]}")
                case "PullRequestEvent":
                    print(f"Had Pull Request activity {event["amount"]} {check_plural(event, "time")} on {event["name"]}")
                case "PullRequestReviewEvent":
                    print(f"Reviewed Pull Request {event["amount"]} {check_plural(event, "time")} on {event["name"]}")
                case "PullRequestReviewCommentEvent":
                    print(f"Gave {event["amount"]} {check_plural(event, "comment")} for Pull requests on {event["name"]}")
                case "PullRequestReviewThreadEvent":
                    print(f"Gave {event["amount"]} {check_plural(event, "comment")} for Pull request comments on {event["name"]}")
                case "PushEvent":
                    print(f"Pushed {event["amount"]} {check_plural(event, "commit")} on {event["name"]}")
                case "ReleaseEvent":
                    print(f"Released {event["amount"]} {check_plural(event, "commits")} on {event["name"]}")
                case "SponsorshipEvent":
                    print(f"Gave {event["amount"]} Sponsorship {check_plural(event, "listing")} on {event["name"]}")
                case "WatchEvent":
                    print(f"Starred {event["amount"]} {check_plural(event, "repository")} on {event["name"]}")
    
                

def check_plural(event, word):
    if event["amount"] > 1:
        if word.endswith("h"):
            return word + "es"
        elif word.endswith("y"):
            new_word = word[:-1]
            return new_word + "ies"
        else:
            return word + "s"
    else:
        return word
        

def filter_type(final_output):
    list_of_types = ["CreateCommitEvent","CreateEvent","DeleteEvent","ForkEvent","GollumEvent","IssueCommentEvent","IssuesEvent",
                     "MemberEvent","PublicEvent","PullRequestEvent","PullRequestReviewEvent","PullRequestReviewCommentEvent",
                     "PullRequestReviewThreadEvent","PushEvent","ReleaseEvent","SponsorshipEvent","WatchEvent"]
    user = input("Would you like to filter by a certain type or types(Yes/No): ")
    if user == "Yes":
        print("Please enter the types you want to search for:")
        print("List of available types:")
        for type in list_of_types:
            print(type)
        user_types = input("If searching for multiple types, seperate each one with a space:")
        split_types = user_types.split()
        progressing, filtered_types = process_types(split_types, list_of_types)
        if progressing == False:
            filtering_types = True
            give_output(final_output, filtering_types, filtered_types)
            print("Done")
            return True
    elif user == "No":
        filtering_types = False
        filtered_types = None
        give_output(final_output, filtering_types, filtered_types)
    else:
        print("command is not valid, try again") 

def process_types(user_types, list):
    lowercase_list = [s.lower() for s in list]
    for f_type in user_types:
        lower_f_type = f_type.lower()
        if lower_f_type not in lowercase_list:
            print(f"{f_type} is not a valid event, please try again")
    else:
        print("done")
        progressing = False
        return progressing, user_types

    
def retry():
    user = input("Would you like to restart again: ")
    match user.lower():
        case "yes":
            return True
        case "no":
            return False
        case _ :
            print("not valid, please try again")

def main():
    while True:
        username = input("Please enter a username: ").lower()
        url = f"https://api.github.com/users/{username}/events"
        r = requests.get(url)
        events = r.json()
        filtering_types = False
        event_dict, event_name_check, event_type_check = search_for_values(r,events)
        final_output = output_sets(event_dict, event_name_check, event_type_check)
        filter_type(final_output)
        if not retry():
            break

main()
    

#Work on making output fancy tomorrow
