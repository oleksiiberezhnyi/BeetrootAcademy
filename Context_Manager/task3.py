import pytest
import typing


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


@pytest.fixture
def data_first_name():
    return "Oleksii"


@pytest.fixture
def data_last_name():
    return "Berezhnyi"


@pytest.fixture
def data_email_name():
    return "mail@me.com"


@pytest.fixture
def data_phone_name():
    return 380731737373


def test_user_data(data_first_name, data_last_name, data_email_name,
                   data_phone_name):
    assert user_data(data_first_name, data_last_name, data_email_name,
                     data_phone_name) \
           == ["O.", "Berezhnyi", "Oleksii Berezhnyi", "mail@me.com",
               380731737373]
