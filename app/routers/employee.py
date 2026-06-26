from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas import EmployeeCreate
from app.models import Employee
from app.dependencies import get_db

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)

# CREATE
@router.post("/")
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    new_employee = Employee(
        name=employee.name,
        email=employee.email,
        department=employee.department
    )

    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)

    return new_employee

# GET ALL
@router.get("/")
def get_all_employees(db: Session = Depends(get_db)):
    return db.query(Employee).all()

# GET BY ID
@router.get("/{id}")
def get_employee(id: int, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.id == id).first()

    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    return employee

# UPDATE
@router.put("/{id}")
def update_employee(id: int, employee: EmployeeCreate, db: Session = Depends(get_db)):
    emp = db.query(Employee).filter(Employee.id == id).first()

    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")

    emp.name = employee.name
    emp.email = employee.email
    emp.department = employee.department

    db.commit()
    db.refresh(emp)

    return emp

# DELETE
@router.delete("/{id}")
def delete_employee(id: int, db: Session = Depends(get_db)):
    emp = db.query(Employee).filter(Employee.id == id).first()

    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")

    db.delete(emp)
    db.commit()

    return {"message": "Employee deleted successfully"}