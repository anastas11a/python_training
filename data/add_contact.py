from model.contact import Contact
import random
import string

constant = [
    Contact(firstname="name1", lastname="lastname1", middlename="middlename1"),
    Contact(firstname="name2", lastname="lastname2", middlename="middlename2")
]

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