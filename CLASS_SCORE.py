class score:
    def __init__(self):
        self.math=80
        self.chinese=70
        self.physical=75
        self.english=85
        self.geography=83
    
    def score1(self):
        print("my math score:",self.math)
    

    def vote(self):
        if self.chinese>80:
            print("you like god")
        else:
            print("you loss")

   

obj=score()
obj.score1()

obj.vote()