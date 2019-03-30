__author__ = 'Sergey Khrul'

from models.group import Group
from random import randrange
from random import choice
import string


const_data = [
    Group(name='name1', header='header1', footer='footer1'),
    Group(name='name2', header='header2', footer='footer2'),
]

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


test_data = [Group()] + [random_group() for x in range(10)]

# test_data = random_group_list()