from model.contact import Contact
import random
import string
import os.path
import json
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 2
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a



def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_numbers(maxlen):
    symbols = string.digits
    return ([random.choice(symbols) for i in range(maxlen)])

testdata = [
    Contact(firstname=random_string("fistname", 10), middlename=random_string("middlename", 5), lastname=random_string("lastname", 15),
            nickname=random_string("nickname", 7), title=random_string("title", 10),
            company=random_string("company", 10), address=random_string("address", 15), homephone=random_numbers(7),
            mobilephone=random_numbers(7), workphone=random_numbers(10),
            fax=random_string("fax", 10), email1=random_string("email1", 10), email2=random_string("email2", 10),
            email3=random_string("email3", 10), homepage=random_string("homepage", 10), address2=random_string("address2", 10), phone2=random_numbers(7),
            notes=random_string("notes", 10))
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))