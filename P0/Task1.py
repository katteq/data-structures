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


# We have to count all numbers so the dictionary is initialized outside the function


numbers_dictionary={}

def count_phone_numbers(list, numbers):
    for sending_number, receiving_number, *other in list:
        if numbers.get(sending_number) == None:
            numbers[sending_number] = sending_number
        if numbers.get(receiving_number) == None:
            numbers[receiving_number] = receiving_number

    return len(numbers)

print("There are %s different telephone numbers in the records." %
    (count_phone_numbers(texts, numbers_dictionary) + count_phone_numbers(calls, numbers_dictionary)))
