from models.group import Group
from random import randrange
from random import choice
import string
import os.path
import json
import getopt
import sys

__author__ = 'Sergey Khrul'

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["Number of groups", "File path"])
except getopt.GetoptError as err:
    # print help information and exit:
    print
    str(err)  # will print something like "option -a not recognized"
    getopt.usage()
    sys.exit(2)

n = 5
f = "data_provider/data/groups.json"

def random_string(prefix, maxlen):
    '''Generate random symbols
    @:return string'''
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    rnd_string = ''.join([choice(symbols) for i in range(randrange(maxlen))])
    return prefix + rnd_string


def random_group(name_len=10, header_len=20, footer_len=20):
    '''Generate random Group
    @:return Group'''
    name = random_string('name_', name_len)
    header = random_string('header_', header_len)
    footer = random_string('footer_', footer_len)
    return Group(name=name, header=header, footer=footer)


def random_group_list(len = 5, name_len=10, header_len=20, footer_len=20):
    '''Generate random Test Groups Data
    @:return Group'''
    grouplist = [
        Group(name=name, header=header, footer=footer)
        for name in [None, random_string('name_', name_len)]
        for header in [None, random_string('header_', header_len)]
        for footer in [None, random_string('footer_', footer_len)]
    ]
    return grouplist



test_data = [Group()] + [random_group() for x in range(n)]

file_data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
file_data_path = os.path.join(file_data_dir, f)

# if not os.path.exists(file_data_dir):
#     os.makedirs(file_data_dir)

with open(file_data_path, 'w') as f:
    f.write(json.dumps(test_data, default=lambda x: x.__dict__, indent=2))
