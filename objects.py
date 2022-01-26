class vector:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

class new:
    def __init__(self,class_name='none',position=vector()):
        self.type = class_name
        self.pos = position
        symbols = {
            'apple': '🍎',
            'snake_head': '😛',
            'snake_tail': '🟨',
            'wall': '🟫',
            'nothing': '🟩' 
        }
        if class_name in symbols:
            self.symbol = symbols[class_name]
        else:
            self.symbol = symbols['nothing']