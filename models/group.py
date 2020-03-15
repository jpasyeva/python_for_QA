from sys import maxsize


class Group:

    def __init__(self, name_group=None, header=None, footer=None, id_group=None):
        self.name_group = name_group
        self.header = header
        self.footer = footer
        self.id_group = id_group

    def __repr__(self):
        return "%s:%s:%s:%s" % (self.id_group, self.name_group, self.header, self.footer)

    def __eq__(self, other):
        return (self.id_group is None or other.id_group is None or self.id_group == other.id_group) and self.name_group == other.name_group

    def id_or_max(self):
        if self.id_group:
            return int(self.id_group)
        else:
            return maxsize
