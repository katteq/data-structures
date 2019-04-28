"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

def get_phone_area_code(phone_number):
  if phone_number.startswith("140"):
    return 140

  match_fixed = re.search('^\\((\d+)\\)+', phone_number)
  if match_fixed and match_fixed.group(1):
    return match_fixed.group(1)

  match_mobile = re.search('^([7|8|9]\d{3})', phone_number)
  if match_mobile and match_mobile.group(0):
    return match_mobile.group(0)

  return None

def find_recepients_area_codes(list):
  recepients_codes = {}
  total = 0

  for sending_number, receiving_number, _, _ in list:
    sending_number_code = get_phone_area_code(sending_number)
    if sending_number_code != None and sending_number_code == "080":
      receiving_number_code = get_phone_area_code(receiving_number)
      if receiving_number_code != None:
        if receiving_number_code not in recepients_codes:
          recepients_codes[receiving_number_code] = 0
        recepients_codes[receiving_number_code] += 1
        total += 1

  return (recepients_codes, total)

recepients_area_codes, calls_total_number = find_recepients_area_codes(calls)

recepients_area_codes_list = list(recepients_area_codes)
recepients_area_codes_list.sort()

print("The numbers called by people in Bangalore have codes:")
print(*recepients_area_codes_list, sep = "\n")

bangalore_calls = int(recepients_area_codes['080'])/int(calls_total_number) * 100

print("%.2f percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore." % bangalore_calls)
