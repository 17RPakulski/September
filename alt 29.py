
starting_year = []
starting_year_user = int(input('Input Year: '))

cPop = []
starting_population_user = int(input('Input current population: '))

starting_year.append(starting_year_user)
cPop.append(starting_population_user)




cDeath = int(input('Input current death rate: '))
cBirth = int(input('Input current birth rate: '))
cMigration = int(input('Input current migration: '))

pDeath = int(input('Input death rate per year per 1000 population: '))
pBirth = int(input('Input birth rate per year per 1000 population: '))
pMigration = int(input('Input migration rate per year per 1000 population: '))

years = int(input('How many years do you want to model?'))

for i in range(years):
    cPop.append(cPop[i]
    - cPop[i]*(cDeath/1000)
    + cPop[i]*(cBirth/1000)
    + cPop[i]*(cMigration/1000))
    
    
print(cPop)




