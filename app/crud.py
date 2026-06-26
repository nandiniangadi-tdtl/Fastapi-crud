from app.models import Employee

def create_employee(db, employee):

    db.add(employee)

    db.commit()

    db.refresh(employee)

    return employee

def get_all(db):

    return db.query(Employee).all()

def get_by_id(db, emp_id):

    return db.query(Employee).filter(Employee.id == emp_id).first()

def update_employee(db, emp_id, data):

    employee = get_by_id(db, emp_id)

    employee.name = data.name

    employee.email = data.email

    employee.department = data.department

    db.commit()

    db.refresh(employee)

    return employee

def delete_employee(db, emp_id):

    employee = get_by_id(db, emp_id)

    db.delete(employee)

    db.commit()

    return employee



