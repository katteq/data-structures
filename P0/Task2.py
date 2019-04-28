"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""

def find_number_with_longest_calls_time(list):
    numbers = {}
    max_time = 0
    phone_number = None

    for sending_number, receiving_number, _, duration in list:
        if numbers.get(sending_number) == None:
            numbers[sending_number] = 0

        if numbers.get(receiving_number) == None:
            numbers[receiving_number] = 0

        numbers[sending_number] += int(duration)
        numbers[receiving_number] += int(duration)

        if numbers[sending_number] > max_time:
            max_time = numbers[sending_number]
            phone_number = sending_number

        if numbers[receiving_number] > max_time:
            max_time = numbers[receiving_number]
            phone_number = receiving_number

    return (phone_number, max_time)


print("%s spent the longest time, %s seconds, on the phone during September 2016." % find_number_with_longest_calls_time(calls))
