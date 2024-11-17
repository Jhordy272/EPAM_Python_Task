class Dictionary:
    # Constructor
    def __init__(self):
        self.dictionary = {}

    # Add a new entry to the dictionary
    def newentry(self,key,value):
        self.dictionary[key] = value

    # Look up a key in the dictionary
    def look(self,key):
        return self.dictionary.get(key, "Can't find entry for " + key)