
from model.group import Group
import random
import string

testdata = [
     Group(name="test1", header="testtest1", footer="testtesttest1"),
     Group(name="test2", header="testtest2", footer="testtesttest2")
 ]

# constant = [
#     Group(name="test1", header="testtest1", footer="testtesttest1"),
#     Group(name="test2", header="testtest2", footer="testtesttest2")
# ]
#
# def random_string(prefix, maxlen):
#     # symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
#     symbols = string.ascii_letters + string.digits + " " * 10
#     return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
#
#
# testdata = [Group("", "", "")] + [
#     Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
#     for i in range(5)
#     # Group(name="test", header="testtest", footer="testtesttest")
#     # Group("", "", "")
# ]