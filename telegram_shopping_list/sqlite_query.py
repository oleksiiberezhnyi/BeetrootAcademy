from sqlalchemy import create_engine, desc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, VARCHAR, REAL, TEXT
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///shopping_list.db", echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    telegram_id = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Users(" \
               f"id={self.id}, " \
               f"telegram_id={self.telegram_id}" \
               f")>"

    def __str__(self):
        return f"id={self.id}, " \
               f"telegram_id={self.telegram_id}"


class Lists(Base):
    __tablename__ = "lists"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(TEXT, nullable=False)
    user_tg_id = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Lists(" \
               f"id={self.id}, " \
               f"title={self.title}, " \
               f"user_tg_id={self.user_tg_id}" \
               f")>"

    def __str__(self):
        return f"id={self.id}, " \
               f"title={self.title}, " \
               f"user_tg_id={self.user_tg_id}"


class Goods(Base):
    __tablename__ = "goods"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(TEXT, nullable=False)
    quantity = Column(REAL, default=1)
    list_id = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Goods(" \
               f"id={self.id}, " \
               f"name={self.name}, " \
               f"quantity={self.quantity}, " \
               f"list_id={self.list_id}" \
               f")>"

    def __str__(self):
        return f"id={self.id}, " \
               f"name={self.name}, " \
               f"quantity={self.quantity}, " \
               f"list_id={self.list_id}"



def db_create(engine):
    Base.metadata.create_all(engine)


def db_clear():
    for _ in session.query(Users).all():
        session.delete(_)
    for _ in session.query(Lists).all():
        session.delete(_)
    for _ in session.query(Goods).all():
        session.delete(_)
    session.commit()


def check_user(telegram_id):
    return session.query(Users).\
            filter(Users.telegram_id == telegram_id).\
            count() == 0


def add_user(telegram_id):
    if check_user(telegram_id):
        new_user = Users(telegram_id=telegram_id)
        try:
            session.add(new_user)
            session.commit()
        except:
            session.rollback()


# def check_list_name(title, user_tg_id):
#     try:
#         return session.query(Lists.id).\
#             filter(Lists.user_tg_id == user_tg_id, Lists.title == title).\
#             count()
#     except:
#         return False


def create_list(title, user_tg_id):
    # if check_list_name(title, user_tg_id) is False:
    new_list = Lists(title=title, user_tg_id=user_tg_id)
    try:
        session.add(new_list)
        session.commit()
    except:
        session.rollback()


def view_all_lists(user_tg_id):
    try:
        return session.query(Lists.id, Lists.title).\
            filter(Lists.user_tg_id == user_tg_id).\
            all()
    except:
        list()


def view_list(title, user_tg_id):
    return session.query(Lists).\
        filter(Lists.user_tg_id == user_tg_id, Lists.title == title).\
        all()


def delete_all_lists(user_tg_id):
    for _ in session.query(Lists).\
            filter(Lists.user_tg_id == user_tg_id).\
            all():
        session.delete(_)
    try:
        session.commit()
    except:
        session.rollback()


def delete_list(title, user_tg_id):
    temp = session.query(Lists).\
            filter(Lists.user_tg_id == user_tg_id, Lists.title == title).\
            all()
    session.delete(temp)
    try:
        session.commit()
    except:
        session.rollback()


def add_goods(name, list_id, count = 1):
    new_good = Goods(name=name, list_id=list_id, count=count)
    try:
        session.add(new_good)
        session.commit()
    except:
        session.rollback()

def get_list_id(user_tg_id, title):
    return session.query(Lists.id).\
            filter(Lists.user_tg_id == user_tg_id, Lists.title == title).first()

def view_all_goods(list_id):
    return session(Goods).\
            filter(Goods.list_id == list_id).\
            all()


def delete_goods(name, list_id):
    pass


if __name__ == "__main__":
    # print(check_user(123))
    # add_user(123)
    # print(check_list_name("test1", 123))
    # create_list("test1", 123)
    # db_create(engine)
    print(view_all_lists(123))
    pass