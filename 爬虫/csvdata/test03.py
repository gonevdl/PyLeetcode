import json
from country import get_ccountry_name

with open("population_data.json") as p:
    pop_data = json.load(p)

for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_ccountry_name(country_name)
        # print(country_name + ": " + str(population))
        if code:
            print(code + ": " + str(population))
        else:
            print("ERROR - " + country_name)
