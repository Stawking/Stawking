import linecache as lc
import random as rd
import copy

"""
Purpose: Hangman art :)
"""  
ASCII_ART = {
    0:"""
*       ___________            *
*        |/      |             *
*        |      (_)            *
*        |      /|\\            *
*        |       |             *
*        |      / \\            *
*        |                     *
*       _|_____________        *               
    """,
    1:"""
*       ___________            *
*        |/      |             *
*        |      (_)            *
*        |      /|\\            *
*        |       |             *
*        |      /              *
*        |                     *
*       _|_____________        *               
    """,
    2:"""
*       ___________            *
*        |/      |             *
*        |      (_)            *
*        |      /|\\            *
*        |       |             *
*        |                     *
*        |                     *
*       _|_____________        *               
    """,
    3:"""
*       ___________            *
*        |/      |             *
*        |      (_)            *
*        |      /|\\            *
*        |                     *
*        |                     *
*        |                     *
*       _|_____________        *               
    """,
    4:"""
*       ___________            *
*        |/      |             *
*        |      (_)            *
*        |      /|             *
*        |                     *
*        |                     *
*        |                     *
*       _|_____________        *               
    """,
    5:"""
*       ___________            *
*        |/      |             *
*        |      (_)            *
*        |       |             *
*        |                     *
*        |                     *
*        |                     *
*       _|_____________        *               
    """,
    6:"""
*       ___________            *
*        |/      |             *
*        |      (_)            *
*        |                     *
*        |                     *
*        |                     *
*        |                     *
*       _|_____________        *               
    """,
    7:"""
*       ___________            *
*        |/      |             *
*        |                     *
*        |                     *
*        |                     *
*        |                     *
*        |                     *
*       _|_____________        *               
    """,
}


"""
Purpose: File Reader
"""
class WordList:
    FILE_PATH = 'words.txt'
    LINE_COUNT = 854
    
    @classmethod
    def getword(cls) -> str:  
        random_line = rd.randrange(1, cls.LINE_COUNT)
        word = lc.getline(cls.FILE_PATH, random_line)
        lc.clearcache()
        #linecache module does not raise an exception on its own, instead returning ''
        if not word: raise FileNotFoundError("Line could not be found")
        return word.upper().strip()

"""
Purpose: Holds all game info and handles updating data
DOES NOT HANDLE STRING FORMATTING OR INPUT VALIDATION
"""
class HangMan:
    def __init__(self):
        self.word = WordList.getword()
        self.score = '_.' * len(self.word)
        self.guessed = set()
        self.lives = 7
        self.over = False
    
    def guess(self, letter:str) -> bool:
        if self.over: return False
        if letter in self.guessed: return False
    
        self.guessed.add(letter)
        old_score = copy.deepcopy(self.score)
        for index, character in enumerate(self.word):
            if character == letter:
                self.score = self.score[:index*2] + letter + self.score[index*2 + 1:]
                
        if self.score.replace(".",'') == self.word: 
            self.over = True
        if old_score == self.score: self.lives -=1
        if self.lives < 1: self.over = True
        
        return True
        
"""
Purpose: Continously prompts user for input, validates that input, and parses the results.
"""    
def gameloop():
    game = HangMan()
    while not game.over:
        print(ASCII_ART[game.lives])
        print(f"        {game.score}\n")
        guess = input("Please guess a letter: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if not game.guess(guess): print("You already guessed that!")
        else:
            print("Invalid guess!")
    
    if game.lives > 0: print("\n YOU WIN!!!!")
    else: print(f"\n You lost. The word was: {game.word}")
    print(ASCII_ART[game.lives])
    print(f"        {game.score}\n")


"""
Purpose: run our scripts
"""    
def main():
    print("Ready to play Hangman?")
    gameloop()
    while input("Play Again? Enter 'Y': ").upper() == 'Y':
        gameloop()


if __name__ == "__main__":
    main()
