from sys import maxsize

__author__ = 'Sergey Khrul'


GROUP_PRINT_FORMAT = "{id} - Name: {name}."


class Group:
    def __init__(self, _id=None, name=None, header=None, footer=None):
        self.id = _id
        self.name = name
        self.header = header
        self.footer = footer

    def __repr__(self):
        return GROUP_PRINT_FORMAT.format(id=self.id, name=self.name)

    def __eq__(self, other):
        return self.name == other.name and (self.id is None or other.id is None or self.id == other.id)

    def id_or_max(grp):
        if grp.id:
            return int(grp.id)
        return maxsize

