from Document import Document
import math
class Ranking():
    
    
    docDic = 0

    
    @staticmethod
    def TermFrequency(word):
        TF = {}
        wordDic = {}
        docData = Document.docData
        k = Document.Search(word)
        for key,val in k.items():
            wordDic[key] = len(val)
            TF[key] = len(val)/docData[key]
            if len(val)>0:
                Ranking.docDic = Ranking.docDic+1
            
        return TF

    @staticmethod
    def inverseDocumentFrequency():
        if(Ranking.docDic!=0):
            return math.log(10/Ranking.docDic)
        else:
            return 0
    
  
    @staticmethod
    def Rank(word):
        TF = Ranking.TermFrequency(word)
        IDF = Ranking.inverseDocumentFrequency()
        for key in TF:
            TF[key] = TF[key]*IDF
        return TF
        
       

           

  


