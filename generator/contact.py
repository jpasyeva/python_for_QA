import random
import string
import jsonpickle
import os.path
import getopt
import sys
from models.contact import Contact


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f", ["number of contacts", "file"])
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


testdata = [Contact(firstname="", lastname="", address="", home_phone="", mobile_phone="", work_phone="",
                    email="", email2="", email3="", address2="", phone2="")] + [
    Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 10),
            address=random_string("address", 10),
            home_phone=random_string("home_phone", 10), mobile_phone=random_string("mobile_phone", 10),
            work_phone=random_string("work_phone", 10),
            email=random_string("email", 10), email2=random_string("email2", 10),
            email3=random_string("email3", 10),
            address2=random_string("address2", 10), phone2=random_string("phone2", 10))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))