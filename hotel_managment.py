hotel = {
  '1': {
    '101': ['George Jefferson', 'Wheezy Jefferson'],
  },
  '2': {
    '237': ['Jack Torrance', 'Wendy Torrance'],
  },
  '3': {
    '333': ['Neo', 'Trinity', 'Morpheus']
  }
}

check_in = input("Good evening. Will you be checking in or out? ('in' or 'out') ").lower()

if check_in == "in":
  floor_number = input("What floor would you like to be on? (1, 2, or 3) ")
  room_number = input("What would you like your room number to be? ")
  if room_number in hotel['1'] or room_number in hotel['2'] or room_number in hotel['3']:
    print("This room is occupied. Please pick another one. ")
  else:
    occupant_number = input("how many people will be staying including yourself? ")
    occupant_names = input("Please give the names of each occupant including yourself. separate each name with a comma. ").split(",")
    hotel[floor_number][room_number] = occupant_names
    print(hotel)
else:
  floor_number = input("What floor are you on? ")
  room_number = input("What is your room number? ")
  try:
    hotel[floor_number].pop(room_number)
    print("You have successfully been checked out of room number {room_number}. Thank you for staying with us!")
    print(hotel)
  except Keyerror:
    print("You have never checked in. Please check in before checking out.")