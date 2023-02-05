countries = ['Netherlands','Nigeria','Jordan','Nepal','Niger','Japan']
capitals = ['Amsterdam','Abuja','Amman','Kathmandu','Niamey','Tokyo']

for country, capital in zip(countries, capitals):
    print(f'The capital of {country} is {capital}.')

print()


# if one has more than the other the zip will stop when it runs out of zipable files
countries = ['Netherlands','Nigeria','Jordan','Nepal','Niger','Japan']
capitals = ['Amsterdam','Abuja','Amman','Kathmandu']

for country, capital in zip(countries, capitals):
    print(f'The capital of {country} is {capital}.')

print()

# This will allow you to continue when you run out of items in the longest list. 
# zip_longest from itertools does this, you just have to specify a fill value
from itertools import zip_longest

for country, capital in zip_longest(countries, capitals, fillvalue = 'Unknown'):
    print(f'The capital of {country} is {capital}.')


# unzipping for the win
countries = ['Netherlands','Nigeria','Jordan','Nepal','Niger','Japan']
capitals = ['Amsterdam','Abuja','Amman','Kathmandu','Niamey','Tokyo']

pairs = list(zip(countries,capitals))
print(pairs)

country, capital = zip(*pairs)
print(country)
print(capital)