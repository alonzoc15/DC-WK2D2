phonebook_dict = {
    'Alice': '703-493-1834',
    'Bob': '857-834-1234',
    'Elizabeth': '484-584-2923'
}

# Print Elizabeth's Phone number.
phonebook_dict['Elizabeth']

# Add an entry to the dictionary
phonebook_dict['Kareem'] = '938-489-1234'

# Delete Alice's phone entry
del phonebook_dict['Alice']

# Change Bob's phone number
phonebook_dict['Bob'] = '968-345-2345'

# Print all the phone entries.
print(phonebook_dict)