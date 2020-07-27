from sys import exit, argv
import csv

def main():
    with open(argv[1]) as db:
        database = csv.DictReader(db)
        header = database.fieldnames
        nobody = True
        str_number = 0
        with open(argv[2]) as seq:
            sequence = seq.readline()
            count = []
            for i in range(len(header)-1):
                count.append(count_repeats(header[i+1], sequence))
            for row in database:
                for i in range(len(header)-1):
                    if count[i] == int(row[header[i+1]]):
                        str_number += 1
                    if str_number == len(header) - 1:
                        suspect = (row[header[0]])
                        nobody = False
                str_number = 0
            if nobody == True:
                print('No match')
            else:
                print(suspect)

def count_repeats(tag, sequence):
    count_symbol = 0
    count_word = 0
    max_count_word = 0
    i = 0
    while i < len(sequence)-len(tag)+1:
        for j in range(len(tag)):
            if sequence[i + j] == tag[j]:
                count_symbol += 1
            else:
                count_symbol = 0
                break
        if count_symbol == len(tag):
            count_word += 1
            i += len(tag) - 1
            count_symbol = 0
            if count_word > max_count_word:
                max_count_word = count_word
        else:
            count_word = 0
            count_symbol = 0
        i += 1
    return max_count_word

main()