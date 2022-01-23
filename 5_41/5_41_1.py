from sqlalchemy import create_engine, or_
from sqlalchemy.orm import Session, aliased
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.sql import func

Base = automap_base()

engine = create_engine("sqlite:///database.db")

Base.prepare(engine)

Employees = Base.classes.employees
Departments = Base.classes.departments
Jobs = Base.classes.jobs
Locations = Base.classes.locations

session = Session(engine)

# Write a query to display the names (first_name, last_name)
# using alias name "First Name", "Last Name" from the table of employees;


def name_surname(sess):
    q = sess.query(Employees.first_name + ' ' + Employees.last_name).all()
    return q


# write a query to get the unique department ID from the employee table
def unique_dep_id(sess):
    q = sess.query(Employees.department_id).distinct(Employees.department_id).all()
    return q


# write a query in SQL to display the first name, last name, department number, and department name for each employee
def employees_plus_departments(sess):
    q = sess.query(Employees.first_name, Employees.last_name, Departments.depart_name, Departments.department_id).join(
        Departments, Departments.department_id == Employees.department_id).all()
    return q


# write a query in SQL to display the first and last name, department, city, and state province for each employee
def employees_plus_department_locations(sess):
    q = sess.query(Employees.first_name, Employees.last_name, Departments.depart_name, Locations.city, Locations.state_province).join(
        Departments, Departments.department_id == Employees.department_id).join(
        Locations, Departments.location_id == Locations.location_id).all()
    return q


# write a query in SQL to display the first name, last name, department number, and department name, for all employees for departments 80 or 40
def departments_40_80(sess):
    q = sess.query(Employees.first_name, Employees.last_name, Departments.department_id, Departments.depart_name).join(
        Departments, Departments.department_id == Employees.department_id).filter(
        or_(Departments.department_id == 40, Departments.department_id == 80)).all()
    return q


# write a query in SQL to display the first name of all employees including the first name of their manager
def employee_plus_manager_names(sess):
    Managers = aliased(Employees)
    q = sess.query(Employees.first_name, Managers.first_name).join(Managers, Employees.manager_id == Managers.employee_id).all()
    return q


# write a query in SQL to display the job title, full name (first and last name ) of the employee,
# and the difference between the maximum salary for the job and the salary of the employee
def job_title_and_salary_difference(sess):
    q = sess.query(Jobs.job_title, Employees.first_name + ' ' + Employees.last_name, Jobs.max_salary - Employees.salary).join(
        Jobs, Employees.job_id == Jobs.job_id).all()
    return q


# write a query in SQL to display the job title and the average salary of employees
def job_average_salary(sess):
    q = sess.query(func.avg(Employees.salary), Jobs.job_title).group_by(Jobs.job_id).join(Jobs, Employees.job_id == Jobs.job_id).all()
    return q


# write a query in SQL to display the full name (first and last name), and
# salary of those employees who work in any department located in London
def london_employees(sess):
    q = sess.query(Employees.first_name + ' ' + Employees.last_name, Employees.salary, Locations.city).join(
        Departments, Employees.department_id == Departments.department_id).join(
        Locations, Departments.location_id == Locations.location_id).filter(
        Locations.city == 'London').all()
    return q


print(name_surname(session))
print(unique_dep_id(session))
print(employees_plus_departments(session))
print(employees_plus_department_locations(session))
print(departments_40_80(session))
print(employee_plus_manager_names(session))
print(job_title_and_salary_difference(session))
print(job_average_salary(session))
print(london_employees(session))
