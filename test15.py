# How to read json file in file in Python :
# First create json file & write some data here i had created student.json for this program
import json
with open (r'D:\PythonInterviewbasics-\student.json') as f:
    data = json.load(f)
print(data)