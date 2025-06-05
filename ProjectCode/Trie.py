from TrieNode import TrieNode
class Trie: 
      
    
    def __init__(self): 
        self.root = self.getNode() 
  
    def getNode(self): 
        
        return TrieNode() 
  
    
    def _charToIndex(self,ch): 
        return ord(ch) 
    
    
    def insert(self,key,link,index1,stopword = False): 
        curr = self.root 
        for char in key: 
            index = self._charToIndex(char) 
            
            if not curr.children[index]: 
                curr.children[index] = self.getNode() 
            curr = curr.children[index] 
        curr.isEndOfWord = True
        curr.isStopWord = stopword
        if link not in curr.link:
            curr.link[link] = [index1]
        else:
            curr.link[link].append(index1)
           
    
    def search(self, key): 
        curr = self.root
        for char in key: 
            index = self._charToIndex(char) 
            if not curr.children[index]:
                return [False,{}]
            curr = curr.children[index] 
           
                
        return [curr.isStopWord,curr.link]


