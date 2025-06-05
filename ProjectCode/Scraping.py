from bs4 import BeautifulSoup
import requests

class Scraping():
    
    text2 = ""

    
    @staticmethod
    def getDataFromWebPage(url):
        code = requests.get(url,stream = True)
        with open("temp.html","wb") as html: 
            html.write(code.content)
        
        data = open("temp.html",'r')
        soup = BeautifulSoup(data, 'html.parser')

        
        for script in soup(["script", "style"]):
            script.extract()    # rip it out

        
        text = soup.get_text()

        
        lines = (line.strip() for line in text.splitlines())
        
        
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        
        
        text = '\n'.join(chunk for chunk in chunks if chunk)        
        
        
        ''.join(e for e in text if e.isalnum())
        
        
        text1 = str(text.encode('Ascii',errors = 'ignore'))
        text2 = text1.replace('\\n',' ').replace('//',' ')
        
        
        Scraping.words = text2.split()
        
        return Scraping.words

    def DocumentData():

        
        return len(Scraping.words)