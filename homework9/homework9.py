import json


# Task 2

def task2():
    phonebook = {}
    i = 1

    name_phonebook = input("Name of the phonebook:\n")

    # Add new entries
    def new_entries():
        first_name = input("Enter first name:\n")
        last_name = input("Enter last name:\n")
        full_name = first_name + last_name
        telephone_number = input("Enter telephone number:\n")
        city = input("Enter city or state:\n")
        phonebook.update({f"Conatact{i}": {"First name": first_name,
                                           "Last name": last_name,
                                           "Full name": full_name,
                                           "Telephone number": telephone_number,
                                           "City": city
                                           }
                          }
                         )
        return phonebook

    # Search entries
    def search_entries(dictionary: dict):
        by_value = input("Enter a search word: \n")
        found = [k for k, v in dictionary.items() if any(by_value in n for n in v.values())]
        return found

    # Update entries
    def update_entries(n):
        first_name = input("Enter first name:\n")
        last_name = input("Enter last name:\n")
        full_name = first_name + last_name
        telephone_number = input("Enter telephone number:\n")
        city = input("Enter city or state:\n")
        phonebook[n]["First name"] = first_name
        phonebook[n]["Last name"] = last_name
        phonebook[n]["Full name"] = full_name
        phonebook[n]["Telephone number"] = telephone_number
        phonebook[n]["City"] = city
        return phonebook

    while True:
        answer = input("What do you want to do?\n"
                       "Add new entries(a), Search by...(s), Delete a record(d), Update a record(u), Exit?: ")
        if answer == "a":
            new_entries()
            i += 1
        elif answer == "s":
            for j in search_entries(phonebook):
                print(phonebook[j])
        elif answer == "d":
            for j in search_entries(phonebook):
                phonebook.pop(j)
                print(phonebook)
        elif answer == "u":
            for j in search_entries(phonebook):
                update_entries(j)
                print(phonebook)
        else:
            break

    with open("phonebook.json", "a") as file:
        json.dump(phonebook, file)
        file.close()
