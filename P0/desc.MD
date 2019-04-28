The text data (text.csv) has the following columns:

sending telephone number (string), receiving telephone number (string), timestamp of text message (string).

The call data (call.csv) has the following columns:

calling telephone number (string), receiving telephone number (string), start timestamp of telephone call (string), duration of telephone call in seconds (string)
def find_markering_phones(calls, texts):
    telemarketers = {}
    receivers = {}
    for data in [calls, texts]:
        for sender_call_phone, receiver_call_phone, *other in data:
            if receiver_call_phone not in receivers:
                receivers[receiver_call_phone] = receiver_call_phone
            if sender_call_phone in receivers and sender_call_phone in telemarketers:
                del telemarketers[sender_call_phone]
            elif sender_call_phone not in receivers and sender_call_phone not in telemarketers:
                telemarketers[sender_call_phone] = sender_call_phone


    print (list(telemarketers), len(list(telemarketers)))
    # print (list(receivers))


find_markering_phones(calls, texts)
