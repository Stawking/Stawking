import random
import copy
import linecache

"""
Purpose: File Reader
"""
class WordList:
    FILE_PATH = 'words.txt'
    LINE_COUNT = 854
    
    @classmethod
    def getword(cls) -> str:  
        random_line = random.randrange(1, cls.LINE_COUNT)
        word = linecache.getline(cls.FILE_PATH, random_line)
        linecache.clearcache()
        #linecache module does not raise an exception on its own, instead returning ''
        if not word: raise FileNotFoundError("Line could not be found")
        return word.upper().strip()

"""
Purpose: Holds all game info and handles updating data.
!DOES NOT HANDLE STRING FORMATTING OR INPUT VALIDATION!
"""
class HangMan:
    def __init__(self):
        self.word = "BANANA" #WordList.getword()
        self.score = '_' * len(self.word)
        self.guessed = set()
        self.lives = 6
        self.over = False
    
    def guess(self, letter:str) -> bool:
        if self.over: return False
        if letter in self.guessed: return False
    
        self.guessed.add(letter)
        old_score = copy.deepcopy(self.score)
        for index, character in enumerate(self.word):
            if character == letter:
                self.score = self.score[:index] + letter + self.score[index + 1:]
                
        if self.score == self.word: self.over = True
        if old_score == self.score: self.lives -=1
        if self.lives < 1: self.over = True
        
        return True
        
        
        
        
        
