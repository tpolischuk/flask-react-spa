import csv
import json

def import_csv_data():
    reader = csv.DictReader(open('./samples/example-data-01.csv'))
    import_count = 0
    for row in reader:
        #INSERT STANDARD
        print(row['STANDARD'])

        #INSERT FULL_CODE
        print(row['FULL_CODE'])

        #INSERT DESCRIPTION
        print(row['DESCRIPTION'])


        #Remove standardized data
        row.pop('STANDARD')
        row.pop('FULL_CODE')
        row.pop('DESCRIPTION')

        #Convert to JSON string and insert into TAG
        variable_tag = json.dumps(row)
        print(str(variable_tag))

        import_count += 1

    print(f'Processed {import_count} standards.')

if __name__ == '__main__':
    import_csv_data()
