from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, DECIMAL, VARCHAR, REAL, NUMERIC
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///hr.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Employees(Base):
    __tablename__ = 'employees'

    employeer_id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(VARCHAR(20))
    last_name = Column(VARCHAR(25))
    email = Column(VARCHAR(25))
    phone_number = Column(VARCHAR(20))
    hire_data = Column(Date)
    job_id = Column(VARCHAR(10), nullable=False)
    salary = Column(DECIMAL)
    commission_pct = Column(REAL)
    manager_id = Column(Integer)
    department_id = Column(Integer)
    Avg_Salary = Column(NUMERIC)

    def __repr__(self):
        return f'<Employees(' \
               f'employeer_id={self.employeer_id}, ' \
               f'first_name={self.first_name}, ' \
               f'last_name={self.last_name}, ' \
               f'email={self.email}, ' \
               f'phone_number={self.phone_number}, ' \
               f'hire_data={self.hire_data}, ' \
               f'job_id={self.job_id}, ' \
               f'salary={self.salary}, ' \
               f'commission_pct={self.commission_pct}, ' \
               f'manager_id={self.manager_id}, ' \
               f'department_id={self.department_id}, ' \
               f'Avg_Salary={self.Avg_Salary}, ' \
               f')>'


employees = Employees()
for instance in session.query(Employees.first_name, Employees.last_name, Employees.department_id).order_by(Employees.first_name):
    print(instance.first_name, instance.last_name, instance.department_id)