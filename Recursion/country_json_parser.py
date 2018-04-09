import json
import os


def open_country_json_file(country):

    file_name = country + '.json'
    file_path = os.path.join('bin', file_name)

    with open (file_path) as file:
        json_data = json.load(file)

    return json_data

# For JSON structure reference
# 3 letter ISO 3166-1 alpha-3 code code     id
# 2 letter ISO 3166-1 alpha-2 code code     iso2Code
# Name                                      name
# Region id                                 region.id
# Region Name                               region.value
# Income Level                              incomeLevel.value
# Lending Type                              lendingType.id
# Capital City                              capitalCity
# Longitude                                 longitude
# Latitude                                  latitude

country_list = [json.strip('.json') for json in os.listdir('bin')]  # list of country JSON files - .json extension
# key is user input and value is converted into the matching json key name
# for nested keys: region id for example, value is a list to work with
keyword_list = {'name': 'name', 'id': 'id', 'iso2code': 'iso2Code', 'region id': ['region','id'],
                'region name': ['region', 'value'], 'income level': ['incomeLevel', 'value'],
                'lending type': ['lendingType', 'id'], 'capital city': 'capitalCity',
                'longitude': 'longitude', 'latitude': 'latitude'}


def country_json_parser(json_data, keyword, query):

    for item in json_data:
        # we only need to work with the list, a country data, not the dictionary with page#... etc
        if isinstance(item, list):
            # example json files contain only one country's data, but for the future expansion with multiple indexes
            for country in item:
                country_name = country['name']
                for key, value in country.items():
                    # for nested values such as region/incomeLevel/lendingType, check the outer key and internal key
                    if isinstance(query, list):     # nested query will be a list instead of a str
                        if key == query[0]:
                            parsed_value = value[query[1]]
                    else:   # else, just match the keyword with the key
                        if key == query:
                            parsed_value = value

    print('<<{}\'s {} is {}.>>\n'.format(country_name, keyword, parsed_value))


def main():

    # loop to make sure user enters what's in the proper list
    while True:
        country = input('Enter a country {}: '.format(str(country_list).upper())).lower()
        if country in country_list:
            break
        else:
            print('Please enter the country name among the list\n')

    while True:
        keyword = input('Enter a keyword to search with\n{}\n'.format(str([key for key in keyword_list.keys()]))).lower()
        if keyword in keyword_list.keys():
            break
        else:
            print('Please enter the keyword within the list\n')

    query = keyword_list[keyword]   # matching value pair
    json_data = open_country_json_file(country)
    country_json_parser(json_data, keyword, query)

    while True:
        quit = input('Would you like to search again? (Y/N) ').upper()
        if quit == 'Y' or quit == 'N':
            return quit
        else:
            print('Please enter Y or N only please\n')


if __name__ == "__main__":
    print("Welcome to Country JSON Parser Program\n")
    while True:
        quit = main()
        if quit == 'N':
            print('Thank you!')
            break
