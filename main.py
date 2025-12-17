import random
import linecache

class WordList:
    FILE_PATH = 'words.txt'
    LINE_COUNT = 854
    
    @classmethod
    def getword(cls) -> str: 
        word = linecache.getline(cls.FILE_PATH, random.randrange(1,cls.LINE_COUNT))
        linecache.clearcache()
        return word.strip()
        
print(WordList.getword())
        
