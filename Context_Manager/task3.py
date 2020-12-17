import pytest
import typing


@pytest.fixture
def user_data(first_name: str,
              last_name: str,
              email: str,
              phone: int
              ) -> typing.List:
    return [f'{first_name[0].capitalize()}.',
            last_name.title(),
            f'{first_name.title()} {last_name.title()}',
            email.lower(),
            phone
            ]


def test_user_data():
    assert user_data() == []
    # a = user_data("Oleksii", "Berezhnyi", "mail@me.com", 380731737373)
    # assert a == ["O.", "Berezhnyi", "Oleksii Berezhnyi", "mail@me.com", 380731737373]


def user_data_v2(first_name: str,
                 last_name: str,
                 email: str,
                 phone: int
                 ) -> typing.List:
    return [f'{first_name[0].capitalize()}.',
            last_name.title(),
            f'{first_name.title()} {last_name.title()}',
            email.lower(),
            phone
            ]


def test_user_data_v2():
    a = user_data_v2("Oleksii", "Berezhnyi", "mail@me.com", 380731737373)
    assert a == ["O.", "Berezhnyi", "Oleksii Berezhnyi", "mail@me.com",
                 380731737373]
