#%% Task 1 - Edit code to print as requested
#/*-PS3: Code Block 1--*/

mountain = 'Denali'
nickname = 'Mt. McKinley'
elevation = 20322 

print (f"{mountain}, formerly known as {nickname}, is {elevation}' above sea level.")


#%% Task 2 - Lists and Iteration
data_folder = str('W:\\859_data\\triangle')
data_list = ["streams.shp", "stream_types.csv", "naip_imagery.tif"]
user_item = "roads.shp"
data_list.append(user_item)

for item in data_list:
    print(data_folder + "\\" + item)

#%% Task 3 - Lists and Iteration
user_numbers = []
for i in range(3): 
    input_num = int(input("Enter an integer"))
    user_numbers.append(input_num)
user_numbers.sort()
print(user_numbers[2])

#%% Task 3 - Lists and Iteration (Challenge)
usernumbers = []
for i in range(3): 
    input_num = int(input("Enter an integer"))
    usernumbers.append(input_num)
usernumbers.sort(reverse=True)
print(usernumbers)