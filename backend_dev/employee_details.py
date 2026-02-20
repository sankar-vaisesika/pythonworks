

# def empoloyee_salary(id):
#     if id in employee:
#         print(employee[id]['e_salary'])
#     else:
#         print("Id is missing")

# empoloyee_salary(101)

#full details


# def employee_details(id):
    
#     if id in employee:
#         print(employee[id])
#     else:
#         print("Id is missing")
# employee_details(101)
employee={
          101:{"e_name":"gokul","e_salary":"30000"},
          102:{"e_name":"sachin","e_salary":"35000"},
          103:{"e_name":"mani","e_salary":"40000"},
          }
def employee_detail(id):

    if id in employee:
        updated_salary=int(input("CHanged salary:"))
        employee[id]["e_salary"]=updated_salary
        salary=int(employee[id]["e_salary"])

        name=employee[id]["e_name"]
        
        da=salary*.10
        hra=salary*.20
        total=salary+da+hra
        tax=total*.05
        final=total-tax

        print("ID:",id)
        print("Name:",name)
        print("Final salary",final)
        print("Tax:",tax)
        print("da:",da)
        print("hra:",hra)
        print("------------------------------")
    else:
        print("ID not found")

employee_detail(101)