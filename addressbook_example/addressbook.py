#! /usr/bin/python
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../hello_py/compiled"))

import addressbook_pb2

# This function fills in a Person message based on user input.
def PromptForAddress(person):
  print(person)
  person.id = int(raw_input("Enter person ID number: "))
  person.name = raw_input("Enter name: ")

  email = raw_input("Enter email address (blank for none): ")
  if email != "":
    person.email = email

  while True:
    number = raw_input("Enter a phone number (or leave blank to finish): ")
    if number == "":
      break

    phone_number = person.phones.add()
    phone_number.number = number

    type = raw_input("Is this a mobile, home, or work phone? ")
    if type == "mobile":
      phone_number.type = addressbook_pb2.Person.PhoneNumber.PhoneType.Value('MOBILE')
    elif type == "home":
      phone_number.type = addressbook_pb2.Person.PhoneNumber.PhoneType.Value('HOME')
    elif type == "work":
      phone_number.type = addressbook_pb2.Person.PhoneNumber.PhoneType.Value('WORK')
    else:
      print "Unknown phone type; leaving as default value."

# Main procedure:  Reads the entire address book from a file,
#   adds one person based on user input, then writes it back out to the same
#   file.
if len(sys.argv) != 2:
  print "Usage:", sys.argv[0], "ADDRESS_BOOK_FILE"
  sys.exit(-1)

print(addressbook_pb2.Person.PhoneNumber.PhoneType.Value('MOBILE'))

address_book = addressbook_pb2.AddressBook()

# Read the existing address book.
try:
  f = open(sys.argv[1], "rb")
  address_book.ParseFromString(f.read())
  f.close()
except IOError:
  print sys.argv[1] + ": Could not open file.  Creating a new one."

# Add an address.
PromptForAddress(address_book.people.add())

# Write the new address book back to disk.
f = open(sys.argv[1], "wb")
f.write(address_book.SerializeToString())
f.close()
