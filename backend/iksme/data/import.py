import csv
import json
import csv
import psycopg2

conn = psycopg2.connect("host=127.0.0.1 dbname=flask_api user=flask_api password=flask_api port=5442")
cur = conn.cursor()

def import_csv_data(file):
    reader = csv.DictReader(open(file))
    import_count = 0
    for row in reader:
        standard = row['STANDARD']
        full_code = row['FULL_CODE']
        description = row['DESCRIPTION']

        #Remove standardized data
        row.pop('STANDARD')
        row.pop('FULL_CODE')
        row.pop('DESCRIPTION')

        #Convert to JSON string and insert into TAG
        variable_tag = json.dumps(row)

        cur.execute(
            "INSERT INTO standard VALUES (%s, %s, %s, %s)",
            (full_code,
            standard,
            variable_tag,
            description)
        )

        import_count += 1

    print(f'Processed {import_count} standards.')
    conn.commit()

if __name__ == '__main__':
    import_csv_data('./samples/example-data-01.csv')
    import_csv_data('./samples/example-data-02.csv')
    import_csv_data('./samples/example-data-03.csv')
