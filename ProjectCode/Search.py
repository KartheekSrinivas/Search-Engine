from Ranking import Ranking
from StopWord import StopWord
class Search():
    
    def Search(query):
        Result = {}
        words = query.split()
        
        for word in words:
            k = Ranking.Rank(word)
            for key in k:
                if not StopWord.Search(word)[0]:
                    if key in Result:
                        Result[key] = Result[key]+k[key]
                    else:
                        Result[key] = k[key]
        return Result