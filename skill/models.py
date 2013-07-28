import os.path
import re
import pandas

datadir = 'skill/data'
pattern = re.compile(r'(?P<source>\w+)_(?P<quantity>\w+)_(?P<unit>\w+)_(?P<period>[\w-]+).png')

def getdata():
    rows = []
    cases= os.listdir(datadir)
    for case in cases:
        for f in os.listdir(os.path.join(datadir, case)):
            path = os.path.join(datadir, case,f)
            match = pattern.search(f)
            row = {
                'source': '',
                'quantity': '',
                'unit': '',
                'period': '',
                'case': case,
                'path': path
            }
            if match:
                row.update(match.groupdict())
            rows.append(row)
    df = pandas.DataFrame.from_dict(rows)
    return df
