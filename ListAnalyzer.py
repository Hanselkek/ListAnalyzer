list_count = 0

class ListAnalyzer:
    def __init__(self, ListName: str):
        global list_count

        list_count += 1

        self.listName = ListName or f"RandList{list_count}"
        self.list = []

    def insert(self, a):
        assert a != None, TypeError
        self.list.append(a)

    def get_count(self):
        return len(self.list)