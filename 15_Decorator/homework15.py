from functools import wraps


# Task 1


class Validate:
    NOT_VALID_PREFIX_CHARACTER = "!#$%&'*+-/=?^_`{|}~"
    NOT_VALID_DOMAIN_CHARACTER = "!#$%&'*+/=?^_`{|}~"

    def __init__(self, email):
        self._email = email

    def validate(self):
        if self._email.find('@') > 0:
            email_prefix, email_domain = self._email.split('@')
            for i in email_prefix:
                for j in self.NOT_VALID_PREFIX_CHARACTER:
                    if i == j:
                        raise Exception(f'Not Valid e-mail address. \
                         Character "{j}" not valid.')
            if email_prefix.find("..") > 0 or email_prefix[0] == '.' or \
                    email_prefix[-1] == '.':
                raise Exception(f"Not Valid e-mail address.")

            for i in email_domain:
                for j in self.NOT_VALID_DOMAIN_CHARACTER:
                    if i == j:
                        raise Exception(
                            f'Not Valid e-mail domain. \
                            Character "{j}" not valid.')
            if email_prefix.find("..") > 0 or email_prefix[0] == '.' or \
                    email_prefix[-1] == '.':
                raise Exception(f"Not Valid e-mail address.")
            if email_domain.find(".") > 0:
                domain_name, domain_zone = email_domain.split('.')
                if len(domain_zone) < 2:
                    raise Exception("Not valid domaine zone")
            print(f'Your email "{self._email}" is valid')
        else:
            raise Exception("Not Valid e-mail address. @ character not found")


mail = Validate('o.v.ber@me.com')
mail.validate()


# Task 2


class Boss:

    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.workers = []

    def __repr__(self):
        return f'Boss("{self.id}",' \
               f'"{self.name}",' \
               f'"{self.company}",' \
               f'"{self.workers}")'

    def __str__(self):
        return f'id = {self.id},' \
               f'name = {self.name},' \
               f'company = {self.company},' \
               f'workers = {self.workers}'

    @property
    def worker(self):
        return f'Boss("{self.id}",' \
               f'"{self.name}",' \
               f'"{self.company}",' \
               f'"{self.workers}")'

    @worker.setter
    def worker(self, info):
        self.workers.append(info)


class Worker:

    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self.boss = boss

    def __repr__(self):
        return f'Worker("{self.id}",' \
               f'"{self.name}",' \
               f'"{self.company}",' \
               f'"{self.boss}")'

    def __str__(self):
        return f'Worker:(id = {self.id},' \
               f'name = {self.name},' \
               f'company = {self.company},' \
               f'boss = {self.boss})'

    def add(self, id_, name, company, boss):
        self.id = id_
        self.name = name
        self.company = company
        self.boss = boss
        Boss.worker = {"id_": self.id,
                       "name": self.name,
                       "company": self.company}


boss1 = Boss(1, "Boss1", "Work1")
boss2 = Boss(3, "Boss3", "Work4")
worker1 = Worker(123, "Oleksii", "home", boss1)
worker2 = Worker(321, "Anton", "home", boss1)
worker3 = Worker(321, "Anton", "home", boss2)
boss1.worker = worker1
boss1.worker = worker2
boss2.worker = worker3
print(boss1, boss2, sep="\n")


# Task 3

class TypeDecorator:

    def to_int(self):
        @wraps(self)
        def converter(*args, **kwargs):
            for arg in args:
                if arg.isnumeric():
                    return int(arg)
                else:
                    return f"It's impossible"

        return converter

    def to_str(self):
        @wraps(self)
        def converter(*args, **kwargs):
            return str(' '.join(args))

        return converter

    def to_bool(self):
        @wraps(self)
        def converter(*args, **kwargs):
            return bool(' '.join(args))

        return converter

    def to_float(self):
        @wraps(self)
        def converter(*args, **kwargs):
            for arg in args:
                try:
                    if arg.find(".") > 0:
                        integer, decimal = arg.split(".")
                        if integer.isnumeric() and decimal.isnumeric():
                            return float(int(integer) + \
                                         int(decimal) / (10 ** len(decimal)))
                        else:
                            return f"It's impossible"
                    elif arg.find(",") > 0:
                        integer, decimal = arg.split(",")
                        if integer.isnumeric() and decimal.isnumeric():
                            return float(int(integer) + \
                                         int(decimal) / (10 ** len(decimal)))
                        else:
                            return f"It's impossible"
                except Exception:
                    return f"It's impossible"

        return converter


@TypeDecorator.to_int
def do_nothing(string: str):
    return string


@TypeDecorator.to_str
def do_nothing2(string: str):
    return string


@TypeDecorator.to_bool
def do_something(string: str):
    return string


@TypeDecorator.to_float
def do_nothing3(string: str):
    return string


assert do_nothing("24") == 24
assert do_nothing2("Berezhnyi Oleksii") == "Berezhnyi Oleksii"
assert do_something("True") == True
assert do_nothing3("24.234") == 24.234
