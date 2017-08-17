import random
import itertools

def printgrid(val):
    print(val[0],'|',val[1],'|',val[2],'\n',val[3],'|',val[4],'|',val[5],'\n',val[6],'|',val[7],'|',val[8], sep='')

if __name__ =='__main__':
    print("Welcome to Tic Tac Toe")
    print("This is a new game. Board numbers are as follows")
    print(" 1 | 2 | 3\n 4 | 5 | 6\n 7 | 8 | 9")
    next = 'Y'
    magic = [8,1,6,3,5,7,4,9,2]
    while(next=='Y'):
        val = ['   ','   ','   ','   ','   ','   ','   ','   ','   ']
        userl = []
        compl = []
        print("Player is X, computer is O")
        pos = [1,2,3,4,5,6,7,8,9]
        win = 0
        n = 0
        while(win==0):
            print("Enter your desired location",pos,": ",end="")
            user = int(input())
            userl.append(magic[user-1])
            if user not in pos:
                print("Invalid. Enter your desired location",pos,": ")
            else:
                pos.remove(user)
                val[user-1] = ' X '
                n = n + 1
                if n<5:
                    comp = random.choice(pos)
                    compl.append(magic[comp-1])
                    val[comp-1] = ' O '
                    pos.remove(comp)
                    print("The computer picked:",comp)
            printgrid(val)
            if n>=3:
                userc = list(itertools.combinations(userl,3))
                for i in range(len(userc)):
                    if sum(userc[i])==15:
                        win = 1
                        print("You win!")
                        break
                compc = list(itertools.combinations(compl,3))
                for i in range(len(compc)):
                    if sum(compc[i])==15:
                        win = 1
                        print("You lose!")
                        break
            if n==5 and win==0:
                print("It is a tie!")
                break
        next = input("New game [Y/N] ? ")
