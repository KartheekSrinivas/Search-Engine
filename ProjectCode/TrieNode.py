class TrieNode: 
    
    def __init__(self): 
        self.children = [None]*256
        self.isEndOfWord = False
        self.isStopWord = False
        
        self.link = {}


