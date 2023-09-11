import csv, os, json
from pathlib import Path

CSV_PATH = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, 'data', 'moddump-logo.android.working.csv'))
OUT_PATH = CSV_PATH.rstrip('.csv') + '.json'

reader = csv.reader(open(CSV_PATH).read().splitlines())

rows = [x for x in reader if x[0] != 'Status']

output = []

for row in rows:
    isworking = row[0].lower()
    
    if isworking != 'fully':
        continue

    uniqueid = row[1]
    name = row[2]
    version = row[3]
    link = row[4]

    data = {
        'name': name,
        'versions': {
            'latest': version,
            'working': version
        },
        'working': isworking,
        'uniqueid': uniqueid,
        'link': {
            'latest': link,
            'working': link
        },
        'notes': ''
    }

    output.append(data)

with open(OUT_PATH, 'w') as f:
    f.write(json.dumps(output, indent=4))
    f.close()