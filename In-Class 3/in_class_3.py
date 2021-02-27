# -*- coding: utf-8 -*-

import pandas as pd
import math
import numpy
df = pd.read_csv("C:/Users/andre/Downloads/crash_data.csv")

# For me to get the names of all the columns
#for record in df:
#    print(record)

#Group the data by Crash ID and make sure we have each of the crashes
crash_ids = df["Crash ID"].unique()
#vehicle_ids = df["Vehicle ID"].unique()
grouped = df.groupby(by="Crash ID")
#Example of how to access each crash's information
#for each in crash_ids:
#   print(test.get_group(each))

# Note all three share a crash ID
crashes = df[df['Record Type'] == 1]
vehicles = df[df['Record Type'] == 2]
# If vehicle ID == 0, they weren't in one during the crash
participants = df[df['Record Type'] == 3]

#(A1) Numbers will reference the type of assessment I'm testing

# Makes sure we have all unique crash IDs (outputs should be equal which they are
# so no further action is needed)
if len(crash_ids) == len(grouped):
    print("All crash IDs are unique")

# Check for duplicate serial nums and remove them if they exist (there are 14)
duplicate_serial_nums = pd.concat(g for _, g in df.groupby("Serial #") if len(g) > 1)

#(A2)
check = False

def data_check(testing, check):
    if check:
        print(testing + 'was incorrect')
    else:
        print(testing + 'was correct')
        check = False

def crash_hr_check(crashes, check):
    for value in crashes['Crash Hour']:
        if (value != 24 and value >= 0 and value <= 23) or (value == 99):
            continue
        else:
            print(value)
            return True
    return False
    
check = crash_hr_check(crashes, check)
data_check('Crash Hour range ', check)
        
def serial_range_check(crashes, check):
    for value in crashes['Serial #']:
        if(value >= 1 and value <= 99999):
            continue
        else:
            print(value)
            return True
    return False

check = serial_range_check(crashes, check)
data_check('Serial # range ', check)

#(A3)
def part_display_check(participants, check):
    p_temp = participants[participants['Vehicle ID'] == 0]
    for each in p_temp['Participant Display Seq#']:
        if each >= 2:
            continue
        else:
            print(each)
            return True
    return False

check = part_display_check(participants, check)
data_check('Participant Display Seq # value of Record Type 2 ', check)

#(A4)

#Drops all 'useless' columns
crashes = crashes.dropna(axis=1, how='all')
vehicles = vehicles.dropna(axis=1, how='all')
participants = participants.dropna(axis=1, how='all')

        
#crash_ids = crash_ids.tolist()
#for each in duplicate_serial_nums["Crash ID"]:
#    crash_ids.remove(each)
    
#crash_ids = numpy.array(crash_ids)

#for each in crash_ids:
#    hold = grouped.get_group(each)
#    print(hold)
    
    
#df = df[df['Crash Year'] == 2019]

# Lines 18-21 check for each Serial #'s existance and that they're an int
# within the range 00001 - 99999
def serial_check(num):
    #print(type(num))
    # has incorrect type (should be char according to documentation but
    # in actuality is a float)
#    if type(num) != 'char':
#        return False
    if num >= 1 and num <= 99999:
        return True
    return False
    
#temp = df['Serial #'].apply(serial_check)
#df = df[temp]

def check_hour(hour):
    if math.isnan(hour):
        return False
    elif hour != 24 or hour <= 23 or hour >= 0 or hour == 99:
        return True
    return False

#temp = df['Crash Hour'].apply(check_hour)
#df = df[temp]

