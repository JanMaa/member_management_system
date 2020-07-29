from PyQt5.QtWidgets import QListWidgetItem

class CustomListItem(QListWidgetItem):
    def __init__(self):
        super().__init__()
        self.sortDate = False
        self.sortName = False

    def __lt__(self, other):
        if self.data(101) == other.data(101):
            if self.data(102) == other.data(102):
                return self.data(103) < other.data(103)
            else:
                return self.data(102) < other.data(102)
        else:
            return self.data(101) < other.data(101)


    def isSortDate(self):
        self.sortDate = True
        self.sortName = False
        return self.sortDate


    def isSortName(self):
        self.sortName = True
        self.sortDate = False
        return self.sortName