from Search import Search
import requests
from bs4 import BeautifulSoup
class PresentingLayer():
    
 
    def FinalPresentation(Query):
        
        D = Search.Search(Query)
        Sort_based_on_ranks = sorted(D, key=D.get, reverse=True)

        for key in Sort_based_on_ranks:
            url = key
            code = requests.get(url,stream = True)
            with open("temp.html","wb") as html: 
                html.write(code.content)
        
            data = open("temp.html",'r')
            soup = BeautifulSoup(data, 'html.parser')
            
            print(soup.h1.get_text()+"\n"+url+"\n\n\n")
           
        if(len(Sort_based_on_ranks)==0):
            print("The webpage doesn't inclued the searched word")
            
