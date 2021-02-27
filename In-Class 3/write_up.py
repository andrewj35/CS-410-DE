#Andrew Wiles CS 410 Data Engineering 1/26/21 In Class Assignment #3

#A
#1. Every group of records (crashes) has a Crash Serial # 
#   Every group of records (crashes) should have a unique Crash ID since it's the primary key
#2. CRASH_HR_NO must be in the range 00-23 or 99, and never 24
#   The Serial # field should be a numeric value between 00001 - 99999
#3. If Record Type 3 (participannt) has no corresponding Record Type 2 (vehicle), its vehicle ID should be zero
#4. Records of same type should have same columns filled out (we'll drop all the repeated, empty columns)
#   Alcohol related crashes should see spikes around holidays
#5. Serial # is unique across all crash record types
#   The CRASH_YR_NO field should be 2019 (as this is 2019's crash report for Oregon Hwy 26)
#6. Every crash is a unique event
#7. Crash frequency are comparitively (to previous years) similarly distributed throughout the year - take into consideration outlier events that can affect data
#  

#B
# Violations:
#   - There are records with duplicate Crash Serial #s which violate the rules set in the 
#     documentation. See below for duplicates
#       code: pd.concat(g for _, g in df.groupby("Serial #") if len(g) > 1)
#
#       Out[57]: 
#           Crash ID  ...  Participant Striker Flag
#       49     1826513  ...                       NaN
#       269    1833867  ...                       NaN
#       305    1834096  ...                       NaN
#       956    1843953  ...                       NaN
#       331    1834655  ...                       NaN
#       936    1843814  ...                       NaN
#       486    1837205  ...                       NaN
#       2514   1855400  ...                       NaN
#       540    1838403  ...                       NaN
#       2534   1855937  ...                       NaN
#       5      1809229  ...                       NaN
#       1229   1846543  ...                       NaN
#       1507   1848512  ...                       NaN
#       2267   1853517  ...                       NaN
#
#       [14 rows x 157 columns]
#   - 

#Notes for me:
#- Record Type 1: PK Crash ID
#- Record Type 2: PK Vehicle ID
#- Record Type 3: PK Participant ID
#    - If Vehicle ID == 0, participant wasn't in any vehicle