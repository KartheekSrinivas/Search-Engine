from StopWord import StopWord
from Document import Document
from Trie import Trie

class InitializeEngine():
    
    
    @staticmethod
    def Initialize():
        
        T = Trie()
        T = StopWord.initialize(T)
        T= Document.initializeData(T)
        return T


