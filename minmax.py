countries = ['Netherlands','Nigeria','Jordan','Nepoal','Niger','Japan']
population = [17_500_00, 198_000_000, 10_000_000, 30_000_000, 24_000_000, 128_000_000]

max(population)
min(countries)

# when comparing strings, it counts the alphabetical order and the lenngth
# of the string
# Niger < Nigeria
# Japan < Niger
# Nepal < Niger

# When comparing tuples, it compares the first index first and once it finds
# the min or max of that it stops looking. 

country_pop = list(zip(countries,population))
min(country_pop) # returns Japan

def get_population(pair):
    country,population = pair
    return population

min(zip(countries,population), key=get_population) #returns jordan as iot should

min(zip(countries,population, key = lambda x: x[1])) # simplifies it using a labda function

min(zip(population, countries)) #does things properly taking into account mijn and max eccenticities

