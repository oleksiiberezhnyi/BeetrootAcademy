import unittest
from unittest.mock import patch
import phonebook9


class TestPhonebook(unittest.TestCase):

    def test_search_entries(self):
        search_result = phonebook9.search_entries({'First name': 'Oleksii',
                                                   'Last name': 'Berezhnyi',
                                                   'Full name': 'Oleksii Berezhnyi',
                                                   'Telephone number': '+380731989555',
                                                   'City': 'Chernihiv'})

        self.assertDictEqual(search_result.found, {"First name": "Oleksii",
                                                   "Last name": "Berezhnyi",
                                                   "Full name": "Oleksii Berezhnyi",
                                                   "Telephone number": "+380731989555",
                                                   "City": "Chernihiv"
                                                   }
                             )


unittest.main()
