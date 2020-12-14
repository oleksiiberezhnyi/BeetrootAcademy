import json

"""
Extend Phonebook application

Functionality of Phonebook application:

    Add new entries 
    Search by first name 
    Search by last name 
    Search by full name
    Search by telephone number
    Search by city or state
    Delete a record for a given telephone number
    Update a record for a given telephone number
    An option to exit the program

The first argument to the application should be the name of the phonebook.
Application should load JSON data, if it is present in the folder with
application, else raise an error. After the user exits, all data should be saved
 to loaded JSON.
 """
phonebook = []


def add_new_entries(first_name, last_name, telephone_number, city,
                    phonebook_name="Default"):
    phonebook.append({"Phonebook name": phonebook_name.title(),
                      "First name": first_name.title(),
                      "Last name": last_name.title(),
                      "Full name": f"{first_name.title()} {last_name.title()}",
                      "Telephone number": telephone_number,
                      "City or state": city.title()
                      }
                     )
    return phonebook


def search_by_first_name(first_name):
    result = []
    for i in phonebook:
        if i.get("First name") == first_name:
            result.append(i)
    return result


def search_by_last_name(last_name):
    result = []
    for i in phonebook:
        if i.get("Last name") == last_name:
            result.append(i)
    return result


def search_by_full_name(full_name):
    result = []
    for i in phonebook:
        if i.get("Full name") == full_name:
            result.append(i)
    return result


def search_by_telephone_number(telephone_number):
    result = []
    for i in phonebook:
        if i.get("Telephone number") == telephone_number:
            result.append(i)
    return result


def search_by_city(city):
    result = []
    for i in phonebook:
        if i.get("City or state") == city:
            result.append(i)
    return result


def delete_a_record_by_telephone_number(telephone_number):
    for i in phonebook:
        if i.get("Telephone number") == telephone_number:
            phonebook.remove(i)
    return phonebook


def update_a_record_by_telephone_number(telephone_number, new_telephone_number):
    for i in phonebook:
        if i.get("Telephone number") == telephone_number:
            i["Telephone number"] = new_telephone_number
    return phonebook


try:
    with open("phonebook.json", "a") as file:
        for i in phonebook:
            json.dump(i, file)
except FileNotFoundError:
    with open("phonebook.json", "a+") as file:
        for i in phonebook:
            json.dump(i, file)
