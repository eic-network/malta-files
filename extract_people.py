import json
import unicodecsv
import glob
from collections import OrderedDict
from cStringIO import StringIO

output_directory = 'entities'
files = glob.glob('companies/*.json')

"""
For the sake of readability, we will consider all the actors as people.
Even though they might be companies, the extracted properties will
still be the same: name, date, status etc.
"""

countries = OrderedDict()
people = list()

for json_file in files:
    with open(json_file) as json_data:
        company = json.load(json_data)
        involved_categories = company['involved_parties'].keys()
        for category in involved_categories:
            for person in company['involved_parties'][category]:
                result = OrderedDict()
                result['name'] = person['name'].strip()
                result['type'] = category
                result['company_id'] = company['company_id'].strip()
                result['company_name'] = company['name'].strip()
                result['registration_date'] = company['registration_date'].strip()
                result['status'] = company['status'].strip()

                if person['nationality'] not in countries.keys():
                    countries[person['nationality']] = list()
                    countries[person['nationality']].append(result)
                else:
                    countries[person['nationality']].append(result)

                result2 = result.copy()
                result2['nationality'] = person['nationality']
                people.append(result2)


with open('{0}/all.json'.format(output_directory), 'w') as outfile:
    json.dump(people, outfile, indent=2)

with open('{0}/all.csv'.format(output_directory), 'w') as outfile:
    writer = unicodecsv.DictWriter(outfile, fieldnames=people[0].keys(), encoding='utf-8')
    writer.writeheader()
    for person in people:
        writer.writerow(person)

countries_list = countries.keys()

for country in countries_list:

    # generate output file names
    outfiles = dict()
    for file_type in ['csv', 'json']:
        outfiles[file_type] = '{0}/{1}/{2}.{1}'.format(
            output_directory,
            file_type,
            country.lower().replace(' ', '_').replace('&', 'and')
            )

    # write JSON files
    with open(outfiles['json'], 'w') as outfile:
        json.dump(countries[country], outfile, indent=2)
        print('Wrote {0}'.format(outfiles['json']))

    # write CSV files
    with open(outfiles['csv'], 'w') as outfile:
        writer = unicodecsv.DictWriter(
            outfile,
            fieldnames=countries[country][0].keys(),
            encoding='utf-8')
        writer.writeheader()
        for person in countries[country]:
            writer.writerow(person)
        print('Wrote {0}'.format(outfiles['csv']))
