from datas import listdata,dictdata

data_of_employees=dictdata["employees"]

for x in data_of_employees:
    print(f"Data of Employee ID at {dictdata["company"]} {x["id"]} and Skills are {x["skills"]}")