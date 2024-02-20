# 1. Korak - kreiranje engine objekta pomocu kojeg se spajamo na bazu
from sqlalchemy import create_engine
# 2. Korak - kreiranje modela, odnosno tablica
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
# 4. Korak - rad s podacima - session
from sqlalchemy.orm import sessionmaker


# 1. Korak - kreiranje engine objekta pomocu kojeg se spajamo na bazu
# engine = create_engine('sqlite:///tvrtka_sa.db', echo=True)
engine = create_engine('sqlite:///tvrtka_sa.db')


# 2. Korak - kreiranje modela, odnosno tablica
Base = declarative_base()
class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    last_name = Column(String(50), nullable=False)
    first_name = Column(String(50))
    email = Column(String(150), nullable=False, unique=True)
    phone = Column(String(50))


class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)


# 3. Korak - kreiranje baze sa svim tablicama
Base.metadata.create_all(engine)


# 4. Korak - rad s podacima - session je kao curson u sqlite3 modulu
Session = sessionmaker(bind=engine)
session = Session()


# 4.1 Korak - dodavanje podataka u bazu INSERT INTO
employees = [
    Employee(last_name='Peric', first_name='Pero', email='pero.peric@email.com', phone='+385 9n 1234567'),
    Employee(last_name='Maric', first_name='Marko', email='marko.maric@email.com', phone='+385 9n 7654321'),
    Employee(last_name='Anic', first_name='Ana', email='ana.anic@email.com', phone='+385 9n 1593578'),
    Employee(last_name='Ivic', first_name='Iva', email='iva.ivic@email.com')
]

for employee in employees:
    session.add(employee)

session.commit()


# 4.2.1 Korak - Citanje iz base - SELECT * FROM employees WHERE last_name LIKE 'Marko'
employee_marko = session.query(Employee).filter_by(last_name='Maric').first()
print(employee_marko.id,
      employee_marko.first_name,
      employee_marko.last_name,
      employee_marko.email,
      employee_marko.phone)


print('\n')
# 4.2.2 Korak - Citanje iz base - SELECT * FROM employees
employees_from_db = session.query(Employee).all()
for employee in employees_from_db:
    print(employee.id,
        employee.first_name,
        employee.last_name,
        employee.email,
        employee.phone)


# 4.3 Korak - Azuriranje podataka u bazi UPDATE
employee = session.query(Employee).filter_by(id=4).first()
employee.phone = '+385 9n 4569821'
session.commit()


# 4.4 Korak - Brisanje podataka u bazi DELETE
employee = session.query(Employee).filter_by(id=2).first()
session.delete(employee)
session.commit()
