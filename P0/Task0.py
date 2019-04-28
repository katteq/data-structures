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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

texts_first_incoming_number, texts_first_receiving_number, texts_first_time = texts[0]

print("First record of texts, %s texts %s at time %s" %
    (texts_first_incoming_number, texts_first_receiving_number, texts_first_time))
calls_first_incoming_number, calls_first_receiving_number, calls_first_time, calls_duration_time = calls[len(calls) - 1]

print("Last record of calls, %s calls %s at time %s, lasting %s seconds" %
    (calls_first_incoming_number, calls_first_receiving_number, calls_first_time, calls_duration_time))
