import objects
from random import randint as random

if __name__ == "__main__":
    SizeX = 10
    SizeY = 10
    Score = 0
    isGameEnded = False
    game = [[objects.new('none',objects.vector(i,g)) for i in range(SizeX)] for g in range(SizeY)]

    snake = [objects.new('snake_head',objects.vector(int((SizeX-1)/2),int((SizeY-1)/2)))]

    def show():
        ll = ""
        for i in game:
            l = ""
            for g in i:
                l += g.symbol
            ll+=f'{l}\n'
        print(ll)

    def move(x=0,y=0):
        global isGameEnded
        if isGameEnded: return
        global Score
        head = snake[0]
        old_pos = head.pos
        nX = head.pos.x + x
        nY = head.pos.y + y
        if 0<=nX<SizeX and 0<=nY<SizeY:
            if game[nY][nX].type not in ['wall','snake_tail']:
                if game[nY][nX].type == 'apple':
                    Score += 1
                    new_tail = objects.new('snake_tail',objects.vector(old_pos.x,old_pos.y))
                    snake.append(new_tail)
                    game[new_tail.pos.y][new_tail.pos.x] = new_tail

                    raX = random(0,SizeX-1)
                    raY = random(0,SizeY-1)
                    while game[raY][raX].type != 'none':
                        raX = random(0,SizeX-1) 
                        raY = random(0,SizeY-1)
                    game[raY][raX] = objects.new('apple',objects.vector(raX,raY))

                    print('Ate an apple')
                for i in range(len(snake)-1,0,-1):
                    opos = snake[i].pos
                    snake[i].pos = snake[i-1].pos
                    game[opos.y][opos.x] = objects.new('none',opos)
                head.pos = objects.vector(nX,nY)
                for part in snake:
                    game[part.pos.y][part.pos.x] = part
                if len(snake) == 1:
                    game[old_pos.y][old_pos.x] = objects.new('none',objects.vector(head.pos.x,head.pos.y))
            else:
                print("OOF you ded")
                print(f"Score: {Score}")
                isGameEnded = True
        show()

    def ask():
        if isGameEnded: return
        m = input("Enter a key:")
        if m == 'w':
            move(0,-1)
        elif m == 's': 
            move(0,1)
        elif m == 'a': 
            move(-1,0)
        elif m == 'd':
            move(1,0)
        elif m == 'q': 
            return
        ask()

    rx = random(0,SizeX-1)
    ry = random(0,SizeY-1)
    game[ry][rx] = objects.new('apple',objects.vector(rx,ry))
    game[snake[0].pos.y][snake[0].pos.x] = snake[0]
    print("Snakon - Snake game but in terminal")
    show()
    ask()
    print("Thanks for playing my game.")
