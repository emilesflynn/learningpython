#%% Task 4.1 
#Create a Python file object, i.e., a link to the file's contents
with open(file='ProblemSet3/data/raw/transshipment_vessels_20180723.csv',mode='r') as file_obj:

    #Read the entire contents into a list object
    line_list = file_obj.readlines()

#Save the contents of the first line in the list of lines to the variable "header_line"
header_line = line_list[0]

#Print the contents of the headerLine
print(header_line)

#%% Task 4.2
#Split the header_line into a list of header items
header_items = header_line.split(',')

#List the index of the mmsi, shipname, and fleet_name values
mmsi_idx = header_items.index('mmsi')
name_idx = header_items.index('shipname')
fleet_idx = header_items.index('fleet_name')

#Print the values
print(mmsi_idx,name_idx,fleet_idx)

#%% Task 4.3
#Create an empty dictionary
vessel_dict = {}

#Iterate through all lines (except the header) in the data file:
for line in line_list[1:]:
    #Split the data into values
    values = line.split(',')

    #Extract the mmsi value from the list using the mmsi_idx value
    mmsi = values[mmsi_idx]

    #Extract the fleet value
    fleet = values[fleet_idx]

    #Adds info to the vesselDict dictionary
    vessel_dict[mmsi] = fleet
    print(len(vessel_dict))

#%% Task 4.4
# Assign the string value 312887000 to a variable named vesselID
vesselID = "312887000"

# Extract the MMSI equal to vesselID value
fleet = vessel_dict.get(vesselID)

# Print using the vesselID and fleet value
print(f"Vessel # {vesselID} flies the flag of {fleet}")

#%% Task 5
# Construct a list of all lines from the contents of the loitering_events_20180723.csv
with open(file='ProblemSet3/data/raw/loitering_events_20180723.csv',mode='r') as f:
    #Read the entire contents into a list object
    vessel_list = f.readlines()
    # Create a Boolean variable, start as False, to track if any vessels meet the criteria
    vessel_found = False

#Loop through each data line
for line in vessel_list[1:]:
    #Split the line string into a list of data items.
    values = line.split(',')

    #Extract item values into their own respective variables
    mmsi = values[0]
    lat1 = float(values[1])
    long1 = float(values[2])
    lat2 = float(values[3])
    long2 = float(values[4])

    # Check if the vessel crosses equator (S to N)
    cross_equator = lat1 < 0 and lat2 > 0

    # Check if vessel ends between 120°E and 135°E longitude
    long2_range = 120 <= long2 <= 135

    # Check if vessel starts between 145°E and 155°E longitude:
    long1_range = 145 <= long1 <= 155

    # if both conditions are met, print the vessel’s mmsi and its fleet from vesselsDict
    if cross_equator and long2_range:
        fleet = vessel_dict.get(mmsi)
        print(f"Vessel # {mmsi} flies the flag of {fleet}")
        # Boolean variable changed to True if any vessels meet the criteria
        vessel_found = True

    if cross_equator and long1_range:
        fleet = vessel_dict.get(mmsi)   
        print(f"Vessel # {mmsi} flies the flag of {fleet}")
        # Boolean variable changed to True if any vessels meet the criteria
        vessel_found = True

# Boolean variable changed to False if all vessels do not meet any criteria
if not vessel_found:
    print("No vessels met criteria")
