# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 10:37:58 2021

@author: andrew wiles
"""

import pandas as pd

dfasc = pd.read_csv('C:/Users/andre/Downloads/CS-410-DE/In-Class 5/acs2017_census_tract_data.csv')
dfcov = pd.read_csv('C:/Users/andre/Downloads/CS-410-DE/In-Class 5/COVID_county_data.csv')
dfasc = dfasc.sort_values(by=['County', 'State'])
dfcov = dfcov.sort_values(by=['county', 'state'])

for item in dfcov['county']:
    if item == 'Bayamon':
        item = 'Bayamón Municipio'
    elif item == 'Bristol Bay plus Lake and Peninsula':
        item = 'Bristol Bay'
    elif item == 'Canovanas':
        item = 'Canóvanas Municipio'
    elif item == 'Catano':
        item = 'Cataño Municipio'
    elif item == 'Comerio':
        item = 'Comerío Municipio'
    elif item == 'Juana Diaz':
        item = 'Juana Díaz Municipio'
    elif item == 'Las Marias':
        item = 'Las Marías Municipio'
    elif item == 'Loiza':
        item = 'Loíza Municipio'
    elif item == 'Manati':
        item = 'Manatí Municipio'
    elif item == 'Mayaguez':
        item = 'Mayagüez Municipio'
    elif item == 'New York City':
        item = 'New York County'
    elif item == 'Rincon':
        item = 'Rincón Municipio'
    elif item == 'San German':
        item = 'San Germán Municipio'
    elif item == 'San Sebastian':
        item = 'San Sebastián Municipio'
    elif item == 'St. John':
        item = 'St. John the Baptist Parish'
    elif item == 'Yakutat plus Hoonah-Angoon':
        item = 'Yakutat City and Borough'

dec_dfcov = dfcov.loc[dfcov['date'].str.startswith('2020-12')]
dec_starting_total_deaths_per_county = dec_dfcov['deaths'].groupby(dec_dfcov['county']).min()
dec_starting_cases_per_county = dec_dfcov['cases'].groupby(dec_dfcov['county']).min()
dec_ending_total_deaths_per_county = dec_dfcov['deaths'].groupby(dec_dfcov['county']).max()
dec_ending_cases_per_county = dec_dfcov['cases'].groupby(dec_dfcov['county']).max()

total_cases = dfcov['cases'].groupby(dfcov['county']).max()
total_deaths = dfcov['deaths'].groupby(dfcov['county']).max()
total_pop = dfasc['TotalPop'].groupby(dfasc['County']).sum()

dfasc = dfasc.drop(columns=['TractId', 'Men', 'Women', 'Hispanic', 'Black', 'Native', 'Asian', 'Pacific', 'VotingAgeCitizen', 'Income', 'IncomeErr', 'White', 'IncomePerCapErr', 'ChildPoverty', 'Professional', 'Office', 'Construction', 'Production', 'Drive', 'Carpool', 'Transit', 'Walk', 'OtherTransp', 'WorkAtHome', 'Service', 'MeanCommute', 'Employed', 'PrivateWork', 'PublicWork', 'SelfEmployed', 'FamilyWork', 'Unemployment'])

asc_counties = pd.DataFrame(columns=('County', 'State', 'Total Pop', 'Income Per Cap', 'Poverty'))
no_dups = []
count = -1
for index, row in dfasc.iterrows():
    # not in DF yet\
    d = ''
    if (row['County'], row['State']) not in no_dups:
        no_dups.append((row['County'], row['State']))
        d = {'County': [row['County']], 'State': [row['State']], 'Total Pop': [row['TotalPop']], 'Income Per Cap': [row['IncomePerCap']], 'Poverty': [row['Poverty']]}
        asc_counties = asc_counties.append(pd.DataFrame(data=d), ignore_index=True)
        count += 1
    # in DF, meaning we need to adjust some values
    else:
        #print(asc_counties[asc_counties[asc_counties['County'] == row['County']]['State'] == row['State']]['Poverty'][0])
        county = row['County']
        state = row['State']
        curr_row = asc_counties.loc[ (asc_counties['County'] == county) & (asc_counties['State'] == state)]
        if pd.notna(row['Poverty']):
            poverty = round(((row['Poverty'] + curr_row['Poverty'])/2), 3)
        else:
            poverty = curr_row['Poverty']
        total_pop = ((row['TotalPop'] + curr_row['Total Pop']))
        if pd.notna(row['IncomePerCap']):
            incomepc = round(((row['IncomePerCap'] + curr_row['Income Per Cap']) / 2), 3)
        else:
            incomepc = curr_row['Income Per Cap']
        
        asc_counties.loc[ (asc_counties['County'] == county) & (asc_counties['State'] == state), ['County', 'State', 'Total Pop', 'Income Per Cap', 'Poverty'] ] = [county, state, total_pop, incomepc, poverty]
        

#for item in dfcov
