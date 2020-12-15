import unittest
import phonebook_v2


class TestPhonebook(unittest.TestCase):

    def test_add_new_entries(self):
        result = phonebook_v2.add_new_entries("Oleksii", "Berezhnyi",
                                              "+380731989555", "Chernihiv",
                                              "Default")
        self.assertListEqual(result, [{'Phonebook name': 'Default',
                                       'First name': 'Oleksii',
                                       'Last name': 'Berezhnyi',
                                       'Full name': 'Oleksii Berezhnyi',
                                       'Telephone number': '+380731989555',
                                       'City or state': 'Chernihiv'
                                       }
                                      ]
                             )

    def test_search_by_first_name(self):
        search_result = phonebook_v2.search_by_first_name("Oleksii")
        search_result2 = phonebook_v2.search_by_first_name("Viktor")
        self.assertListEqual(search_result, [{'Phonebook name': 'Default',
                                              'First name': 'Oleksii',
                                              'Last name': 'Berezhnyi',
                                              'Full name': 'Oleksii Berezhnyi',
                                              'Telephone number': '+380731989555',
                                              'City or state': 'Chernihiv'
                                              }
                                             ]
                             )
        self.assertListEqual(search_result2, [])

    def test_search_by_last_name(self):
        search_result = phonebook_v2.search_by_last_name("Berezhnyi")
        search_result2 = phonebook_v2.search_by_last_name("Berz")
        self.assertListEqual(search_result, [{'Phonebook name': 'Default',
                                              'First name': 'Oleksii',
                                              'Last name': 'Berezhnyi',
                                              'Full name': 'Oleksii Berezhnyi',
                                              'Telephone number': '+380731989555',
                                              'City or state': 'Chernihiv'
                                              }
                                             ]
                             )
        self.assertListEqual(search_result2, [])


unittest.main()
