import csv
from IP_List import *

csv_file_name="full.csv"


with open(csv_file_name, 'w') as file:
    writer = csv.writer(file)
    # IP_Get_List
    for IP in IP_Get_List:
        writer.writerow(["======================================================================================================================================="])
        writer.writerow(["======================================================================================================================================="])
        writer.writerow([IP + "  error data"])
        txt_file_path = "/python_test/" + IP + "/full.txt"
        with open(txt_file_path, "r") as f:
            reader = f.readlines()
        for row in reader:
            writer.writerow([row])
        
