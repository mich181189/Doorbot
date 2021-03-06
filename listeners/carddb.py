import json, os.path

class CardDB:
    def __init__(self, filename):
        self.filename = filename
        self.lastModified = os.path.getmtime(filename)
        self.db = json.load(open(filename, "r"))

    def nickForCard(self, card_serial):
        self.maybeRefresh()
        for entry in self.db:
            if card_serial in entry['cards'] and entry['subscribed'] == True:
                return entry['nick']
        return None

    def maybeRefresh(self):
        timestamp = os.path.getmtime(self.filename)
        if timestamp > self.lastModified:
            print 'refreshing'
            self.lastModified = timestamp
            self.db = json.load(open(self.filename, "r"))
