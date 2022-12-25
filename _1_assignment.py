# program to create a json file with 5 employee details
# Part 1: reading info from a json file and print it into as a list of objects
import json

with open(r"D:\DS291022B\Python\_assignments_python\_6_assignment\employee.json") as file:
    data=json.load(file)
    # print(data)
data_lst=[]
class employee:
    def list_of_json(self,data):
        for rows in data:
            data_lst.append(data[rows])
        return data_lst

obj=employee()
print("Created list from json file: \n\n",obj.list_of_json(data),"\n")

# part 2: Writing a data into json file
dict_obj={
    "TamilNadu": "Chennai",
    "Kerala": "Thiruvananthapuram",
    "Karnataka":"Bengaluru",
    "Goa":"Panaji",
    "Haryana":"Chandigarh",
    "Manipur":"Imphal",
    "Tripura":"Agartala"
}
# json_obj=json.dumps(dict_obj)
# print(json_obj)

with open (r"D:\DS291022B\Python\_assignments_python\_6_assignment\states_capitals.json","w") as file1:
    json.dump(dict_obj,file1)
    



