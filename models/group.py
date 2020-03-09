from sys import maxsize


class Group:

    def __init__(self, name_group=None, header=None, footer=None, id=None):
        self.name_group = name_group
        self.header = header
        self.footer = footer
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.name_group)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name_group == other.name_group

    def id_or_max(self):
        if self.id:
            return self.id
        else:
            return maxsize
