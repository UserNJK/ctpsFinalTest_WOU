'''
3. A file (question_3.txt) contains Integer values where each line represents a list, write a
python program to check whether it contains same number in subsequent position. Display
the count of such occurrences and store the result in a csv file (as shown below).
'''

import csv

count3 = 0

with open('question_3.txt', 'r') as filepath:
    reader = csv.DictReader(filepath)
    for row in reader:
        values = list(row.values())
        for i in range(len(values) - 1):
            if values[i] == values[i + 1]:
                count3 += 1

with open('question_3.txt', 'w', newline='') as filewrite:
    writer = csv.DictWriter(filewrite, fieldnames=reader.fieldnames)
    # Write header if necessary
    writer.writeheader()
    # Write rows
    writer.writerow({})  # Empty row to separate header and data if needed
    writer.writerows(reader)
