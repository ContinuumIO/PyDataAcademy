import csv
from collections import defaultdict
import os.path
import codecs

SOURCE_FILE='data/ODC_STATE_AGENCIES_2012_08_30.txt'
DATA_DIR = 'data'

# Utility class
class UTF8Recoder:
    """
    Iterator that reads an encoded stream and reencodes the input to UTF-8
    """
    def __init__(self, f, encoding):
        self.reader = codecs.getreader(encoding)(f)

    def __iter__(self):
        return self

    def next(self):
        return self.reader.next().encode("utf-8")

rows = None

# 1. Read all rows (we can read it all into memory, it is a small file)

print "preparing module data"

print "reading source file %s" % SOURCE_FILE

with open(SOURCE_FILE) as source:
    recoder = UTF8Recoder(source, "ISO 8859-1")
    reader = csv.reader(recoder, delimiter='|')

    rows = list(reader)

# 2. Split data by year (first column)

print "splitting by year..."
year_data = defaultdict(list)

for row in rows:
    year_data[row[0]].append(row)

print "%d years found" % len(year_data.keys())

# 3. Write files for every year

for year, rows in year_data.items():
    filename = os.path.join(DATA_DIR, "agencies_%s.csv" % year)
    print "writing %s" % filename
    with open(filename, "w") as output:
        writer = csv.writer(output)
        rows = [row[1:] for row in rows]
        writer.writerows(rows)

print "data preparation finished"

