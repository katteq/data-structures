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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def find_markering_phones(calls, texts):
    telemarketers = {}
    receivers = {}

    for sender_text_phone, receiver_text_phone, _ in texts:
        receivers[sender_text_phone] = sender_text_phone
        receivers[receiver_text_phone] = receiver_text_phone

    for sender_phone, receiver_phone, _, _ in calls:
        receivers[receiver_phone] = receiver_phone
        if telemarketers.get(receiver_phone) != None:
            del telemarketers[receiver_phone]
        if receivers.get(sender_phone) != None:
            if  telemarketers.get(sender_phone) != None:
                del telemarketers[sender_phone]
        else:
            telemarketers[sender_phone] = sender_phone

    telemarketers_phones_list = list(telemarketers)
    telemarketers_phones_list.sort()
    return telemarketers_phones_list

print("These numbers could be telemarketers: ")
print(*find_markering_phones(calls, texts), sep = "\n")
