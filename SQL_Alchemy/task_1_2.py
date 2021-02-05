from sqlalchemy import create_engine, desc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Date, DECIMAL, VARCHAR, REAL, NUMERIC
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func


engine = create_engine('sqlite:///hr.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Employees(Base):
    __tablename__ = 'employees'

    employee_id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(VARCHAR(20))
    last_name = Column(VARCHAR(25))
    email = Column(VARCHAR(25))
    phone_number = Column(VARCHAR(20))
    hire_date = Column(Date)
    job_id = Column(VARCHAR(10), nullable=False)
    salary = Column(DECIMAL)
    commission_pct = Column(REAL)
    manager_id = Column(Integer)
    department_id = Column(Integer)
    Avg_Salary = Column(NUMERIC)

    def __repr__(self):
        return f'<Employees(' \
               f'employee_id={self.employee_id}, ' \
               f'first_name={self.first_name}, ' \
               f'last_name={self.last_name}, ' \
               f'email={self.email}, ' \
               f'phone_number={self.phone_number}, ' \
               f'hire_date={self.hire_date}, ' \
               f'job_id={self.job_id}, ' \
               f'salary={self.salary}, ' \
               f'commission_pct={self.commission_pct}, ' \
               f'manager_id={self.manager_id}, ' \
               f'department_id={self.department_id}, ' \
               f'Avg_Salary={self.Avg_Salary}, ' \
               f')>'

    def __str__(self):
        return f'employee_id={self.employee_id}, ' \
               f'first_name={self.first_name}, ' \
               f'last_name={self.last_name}, ' \
               f'email={self.email}, ' \
               f'phone_number={self.phone_number}, ' \
               f'hire_date={self.hire_date}, ' \
               f'job_id={self.job_id}, ' \
               f'salary={self.salary}, ' \
               f'commission_pct={self.commission_pct}, ' \
               f'manager_id={self.manager_id}, ' \
               f'department_id={self.department_id}, ' \
               f'Avg_Salary={self.Avg_Salary}'


class Departments(Base):
    __tablename__ = 'departments'

    department_id = Column(Integer, primary_key=True, nullable=False)
    depart_name = Column(VARCHAR(20), nullable=False)
    manager_id = Column(Integer, nullable=False)
    location_id = Column(Integer)

    def __repr__(self):
        return f'<Departments(' \
               f'department_id={self.department_id}, ' \
               f'depart_name={self.depart_name}, ' \
               f'manager_id={self.manager_id}, ' \
               f'location_id={self.location_id}, ' \
               f')>'

    def __str__(self):
        return f'department_id={self.department_id}, ' \
               f'depart_name={self.depart_name}, ' \
               f'manager_id={self.manager_id}, ' \
               f'location_id={self.location_id}, '


employees = Employees()
departments = Departments()


def display_names():
    for instance in session.query(
            Employees.first_name,
            Employees.last_name
    ):
        print(instance.first_name, instance.last_name)
    session.close()


def unique_department_id(department_id):
    for instance in session.query(Employees)\
            .filter(Employees.department_id == department_id):
        print(instance.first_name, instance.last_name, instance.department_id)
    session.close()


def all_details_ordered_by_first_name(descending=False):
    if descending:
        for instance in session.query(Employees)\
                .order_by(desc(Employees.first_name)):
            print(instance)
    else:
        for instance in session.query(Employees)\
                .order_by(Employees.first_name):
            print(instance)
    session.close()


def get_pf():
    for instance in session.query(
            Employees.first_name,
            Employees.last_name,
            Employees.salary
    ):
        print(
            instance.first_name,
            instance.last_name,
            instance.salary,
            float(instance.salary) * 0.12
        )
    session.close()

def max_and_min_salary():
    for instance in session.query(
            func.max(Employees.salary),
            func.min(Employees.salary)
    ).all():
        print(f'maximum salary {instance[0]}\nminimum salary {instance[1]}')
    session.close()


def monthly_salary():
    for instance in session.query(
            Employees.first_name,
            Employees.last_name,
            Employees.salary
    ):
        print(
            instance.first_name,
            instance.last_name,
            round(float(instance.salary) / 12, 2)
        )
    session.close()


def display_name_with_dep_name():
    for instance in session.query(
            Employees.first_name,
            Employees.last_name,
            Employees.department_id,
            Departments.depart_name)\
            .join(
                Departments,
                Employees.department_id == Departments.department_id
    ):
        print(
            instance.first_name,
            instance.last_name,
            instance.department_id,
            instance.depart_name
        )
    session.close()


def display_name_with_dep_name_for_number(*numbers):
    for number in numbers:
        for instance in session.query(
                Employees.first_name,
                Employees.last_name,
                Employees.department_id,
                Departments.depart_name)\
                .join(
                    Departments,
                    Employees.department_id == Departments.department_id)\
                .filter(Employees.department_id == number
        ):
            print(
                instance.first_name,
                instance.last_name,
                instance.department_id,
                instance.depart_name
        )
    session.close()


def not_include_employee():
    subquery = session.query(Employees.department_id)
    for instance in session.query(
            Departments.depart_name)\
            .filter(Departments.department_id.notin_(subquery)
    ):
        print(
            instance.depart_name
    )
    session.close()


def manager_name():
    subquery = session.query(Employees.first_name)\
        .join(
            Departments,
            Employees.employee_id == Departments.manager_id
    ).subquery()
    for instance in session.query(Employees.first_name, subquery)\
            .join(
                Departments,
                Employees.department_id == Departments.department_id
    ):
        print(instance)


# manager_name()
# not_include_employee()
# display_name_with_dep_name_for_number(40, 80)
# display_name_with_dep_name()
# monthly_salary()
# max_and_min_salary()
# get_pf()
# all_details_ordered_by_first_name()
# unique_department_id(50)
# display_names()
