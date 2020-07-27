from sys import exit, argv
import csv

with open(argv[1]) as database:
    db = csv.DictReader(database)
    with open(argv[2]) as sequence:
        count = []
        for row in db:
            for i in range(len(db.fieldnames)-1):
                count[i] = sequence.count(row[db.fieldnames[i+1]])
                if count[i] == row[db.fieldnames[i+1]]:
                    print([row[0],row[i+1], '= yes'])

