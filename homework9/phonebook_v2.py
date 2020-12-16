import json
import typing


phonebook = []


def add_new_entries(first_name: str,
                    last_name: str,
                    telephone_number: str,
                    city: str,
                    phonebook_name: str = "Default"
                    ) -> typing.List[dict]:
    phonebook.append({"Phonebook name": phonebook_name.title(),
                      "First name": first_name.title(),
                      "Last name": last_name.title(),
                      "Full name": f"{first_name.title()} {last_name.title()}",
                      "Telephone number": telephone_number,
                      "City or state": city.title()
                      }
                     )
    return phonebook


def search_by_first_name(first_name: str) -> typing.List[dict]:
    result = []
    for i in phonebook:
        if i.get("First name") == first_name:
            result.append(i)
    return result


def search_by_last_name(last_name: str) -> typing.List[dict]:
    result = []
    for i in phonebook:
        if i.get("Last name") == last_name:
            result.append(i)
    return result


def search_by_full_name(full_name: str) -> typing.List[dict]:
    result = []
    for i in phonebook:
        if i.get("Full name") == full_name:
            result.append(i)
    return result


def search_by_telephone_number(telephone_number: str) -> typing.List[dict]:
    result = []
    for i in phonebook:
        if i.get("Telephone number") == telephone_number:
            result.append(i)
    return result


def search_by_city(city: str) -> typing.List[dict]:
    result = []
    for i in phonebook:
        if i.get("City or state") == city:
            result.append(i)
    return result


def delete_a_record_by_telephone_number(telephone_number: str) -> typing.List[
    dict]:
    for i in phonebook:
        if i.get("Telephone number") == telephone_number:
            phonebook.remove(i)
    return phonebook


def update_a_record_by_telephone_number(telephone_number: str,
                                        new_telephone_number: str
                                        ) -> typing.List[dict]:
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
