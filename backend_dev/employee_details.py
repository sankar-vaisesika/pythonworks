employee={
          101:{"e_name":"gokul","e_salary":"30000"},
          102:{"e_name":"sachin","e_salary":"35000"},
          103:{"e_name":"mani","e_salary":"40000"},
          }

def empoloyee_salary(id):
    if id in employee:
        print(employee[id]['e_salary'])
    else:
        print("Id is missing")

empoloyee_salary(101)

#full details

def employee_details(id):
    if id in employee:
        print(employee[id])
    else:
        print("Id is missing")
employee_details(101)