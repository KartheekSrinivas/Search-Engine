from Trie import Trie
from StopWord import StopWord
from Scraping import Scraping
class Document():
    T = Trie()
    words = []
    doc = ""
    docData = {}
    @staticmethod
    def initializeData(TrieObject):
        T = TrieObject


        Document.doc = "http://localhost:8000/Input/Page1.html"
        Document.words = Scraping.getDataFromWebPage(Document.doc)
        Document.initialize()
        Document.docData[Document.doc] = Scraping.DocumentData()
        Document.doc = "http://localhost:8000/Input/Page2.html"
        Document.words = Scraping.getDataFromWebPage(Document.doc)
        Document.initialize()
        Document.docData[Document.doc] = Scraping.DocumentData()
        Document.doc = "http://localhost:8000/Input/Page3.html"
        Document.words = Scraping.getDataFromWebPage(Document.doc)
        Document.initialize()
        Document.docData[Document.doc] = Scraping.DocumentData()
        Document.doc = "http://localhost:8000/Input/Page4.html"
        Document.words = Scraping.getDataFromWebPage(Document.doc)
        Document.initialize()
        Document.docData[Document.doc] = Scraping.DocumentData()
        Document.doc = "http://localhost:8000/Input/Page5.html"
        Document.words = Scraping.getDataFromWebPage(Document.doc)
        Document.initialize()
        Document.docData[Document.doc] = Scraping.DocumentData()


        Document.doc= "http://localhost:8000/Input/Page6.html"
        Document.words = Scraping.getDataFromWebPage(Document.doc)
        Document.initialize()
        Document.docData[Document.doc] = Scraping.DocumentData()

        Document.doc = "http://localhost:8000/Input/Page7.html"
        Document.words = Scraping.getDataFromWebPage(Document.doc)
        Document.initialize()
        Document.docData[Document.doc] = Scraping.DocumentData()

        Document.doc = "http://localhost:8000/Input/Page8.html"
        Document.words = Scraping.getDataFromWebPage(Document.doc)
        Document.initialize()
        Document.docData[Document.doc] = Scraping.DocumentData()

        Document.doc = "http://localhost:8000/Input/Page9.html"
        Document.words = Scraping.getDataFromWebPage(Document.doc)
        Document.initialize()
        Document.docData[Document.doc] = Scraping.DocumentData()

        Document.doc = "http://localhost:8000/Input/Page10.html"
        Document.words = Scraping.getDataFromWebPage(Document.doc)
        Document.initialize()
        Document.docData[Document.doc] = Scraping.DocumentData()


        
        return Document.T
    
    #inserting all the scraped data to the Trie object and its method
    @staticmethod
    def initialize():
        for key in range(0,len(Document.words)): 
            k = StopWord.T.search(Document.words[key])[0]
            if not k:
                Document.T.insert(Document.words[key].lower(),Document.doc,key,False) 
                
        
    #returning the key of the word using trie.search
    @staticmethod
    def Search(key):
        return Document.T.search(key)[1]
        

