import random
import linecache

class WordList:
    FILE_PATH = 'words.txt'
    LINE_COUNT = 5
    @staticmethod
    def getword() -> str: 
        word = linecache.getline(WordList.FILE_PATH, random.randrange(1,WordList.LINE_COUNT))
        linecache.clearcache()
        if word:
            return word.strip()
        else:
            print("File/Line does not exist!")
            return 
        
print(WordList.getword())
        
