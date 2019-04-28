"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""


def count_phone_numbers(list):
    numbers={}
    for sending_number, receiving_number, _ in texts:
        if sending_number not in numbers:
            numbers[sending_number] = sending_number
        if receiving_number not in numbers:
            numbers[receiving_number] = receiving_number
    return len(numbers)


print("There are %s different telephone numbers in the records." % (count_phone_numbers(texts) + count_phone_numbers(calls)))
