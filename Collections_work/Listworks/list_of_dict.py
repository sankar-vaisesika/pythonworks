# Sorting a List of Dictionaries by Key

employee=[
    {'name':"Sachin","age":26,"role":"Data analysts"},
    {'name':"Neha","age":24,"role":"Hr"},
    {'name':"Tom","age":29,"role":"QA"},
]

sorted_employee=sorted(employee,key=lambda x:x['age'])

for s in sorted_employee:

    print(s)