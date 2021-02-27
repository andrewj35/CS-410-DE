import pandas as pd

dfasc = pd.read_csv('C:/Users/andre/Downloads/CS-410-DE/In-Class 5/acs2017_census_tract_data.csv')
dfcov = pd.read_csv('C:/Users/andre/Downloads/CS-410-DE/In-Class 5/COVID_county_data.csv')
dfcov = dfcov.sort_values(by=['county'])

test = dfasc.sort_values(by=['County', 'State'])

cov_counties = []
cov_counties_set = set()
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

    if item not in cov_counties_set:
        cov_counties_set.add(item)
        cov_counties.append(item)

cov_counties = sorted(cov_counties, key=str.lower)
#df = pd.DataFrame({'County': cov_counties})

asc_counties = []
asc_counties_set = set()
for item in dfasc['County']:
    if item not in asc_counties_set:
        asc_counties_set.add(item)
        asc_counties.append(item)
        
asc_counties = sorted(asc_counties, key=str.lower)

matching_counties = []
outlier_counties = []
for item in cov_counties:
    if item in asc_counties:
        matching_counties.append(item)
    elif (item + ' County') in asc_counties:
        matching_counties.append((item + ' County'))
    elif (item + ' Parish') in asc_counties:
        matching_counties.append((item + ' Parish'))
    elif (item + ' Municipio') in asc_counties:
        matching_counties.append((item + ' Municipio'))
    elif (item + ' Municipality') in asc_counties:
        matching_counties.append((item + ' Municipality'))
    elif (item + ' Borough') in asc_counties:
        matching_counties.append((item + ' Borough'))
    else:
        outlier_counties.append(item)
        dfcov = dfcov[dfcov['county'] != item]
        cov_counties.remove(item)
        
for item in asc_counties:
    if item not in matching_counties:
        print(item)
# Note: we have 10 outlier values from COV counties list that we cannot place at this time

dfasc = dfasc.drop(columns=['TractId', 'Men', 'Women', 'Hispanic', 'Black', 'Native', 'Asian', 'Pacific', 'VotingAgeCitizen', 'Income', 'IncomeErr', 'White', 'IncomePerCapErr', 'ChildPoverty', 'Professional', 'Office', 'Construction', 'Production', 'Drive', 'Carpool', 'Transit', 'Walk', 'OtherTransp', 'WorkAtHome', 'Service', 'MeanCommute', 'Employed', 'PrivateWork', 'PublicWork', 'SelfEmployed', 'FamilyWork', 'Unemployment'])

dfcov_totals = pd.DataFrame()
prev_county = ""
prev_state = ""
prev_date = ""
total_pop_per_county = dfasc['TotalPop'].groupby(dfasc['County']).sum()
poverty_per_county = dfasc['Poverty'].groupby(dfasc['County']).mean()
incomepercap_per_county = dfasc['IncomePerCap'].groupby(dfasc['County']).mean()

#for county in cov_counties:
    #test = dfcov.loc[dfcov['county'] == county]

dec_dfcov = dfcov.loc[dfcov['date'].str.startswith('2020-12')]
dec_starting_total_deaths_per_county = dec_dfcov['deaths'].groupby(dec_dfcov['county']).min()
dec_starting_cases_per_county = dec_dfcov['cases'].groupby(dec_dfcov['county']).min()
dec_ending_total_deaths_per_county = dec_dfcov['deaths'].groupby(dec_dfcov['county']).max()
dec_ending_cases_per_county = dec_dfcov['cases'].groupby(dec_dfcov['county']).max()

total_cases = dfcov['cases'].groupby(dfcov['county']).max()
total_deaths = dfcov['deaths'].groupby(dfcov['county']).max()
total_pop = dfasc['TotalPop'].groupby(dfasc['County']).sum()

index = 0;
#dec_death_total = dec_ending_total_deaths_per_county[index] - dec_starting_total_deaths_per_county[index]
total_deaths = total_deaths.to_frame()
print(total_deaths.loc[total_deaths['county'] == cov_counties[1920]])
print(list(total_deaths['county']).index(matching_counties[1920]))
dec_death_total = dec_ending_total_deaths_per_county[dec_ending_total_deaths_per_county == matching_counties[index]].index[1] - dec_starting_total_deaths_per_county[dec_starting_total_deaths_per_county == matching_counties[index]].index[1]
dec_case_total = dec_ending_cases_per_county[index] - dec_starting_cases_per_county[index]
state = (dfasc[dfasc['County'] == matching_counties[index]]['State'].iloc[0])
pop = (total_pop[total_pop['County'] == matching_counties[index]]['State'].iloc[0])
print(dfasc[dfasc['County'] == matching_counties[2]]['State'].iloc[0])

d = {'State': state, 'County': cov_counties[index], 'Total Cases': total_cases[index], 'Dec 2020 Cases': [dec_case_total], 'Total Deaths': total_deaths[index], 'Dec 2020 Deaths': [dec_death_total], 'Population': total_pop[index]}
final = pd.DataFrame(data=d)

for each in range ((dec_starting_total_deaths_per_county.size)-1-len(outlier_counties)):
    index = each + 1
    dec_death_total = dec_ending_total_deaths_per_county[dec_ending_total_deaths_per_county == matching_counties[index]].index[0] - dec_starting_total_deaths_per_county[dec_starting_total_deaths_per_county == matching_counties[index]].index[0]
    dec_case_total = dec_ending_cases_per_county[index] - dec_starting_cases_per_county[index]
    state = (dfasc[dfasc['County'] == matching_counties[index]]['State'].iloc[0])
    
    d = {'State': state, 'County': matching_counties[index], 'Total Cases': total_cases[index], 'Dec 2020 Cases': [dec_case_total], 'Total Deaths': total_deaths[index], 'Dec 2020 Deaths': [dec_death_total]}
    final = final.append(pd.DataFrame(data=d))

    
    
    
    
    