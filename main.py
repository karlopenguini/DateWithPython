def LineUpDAte():
    N = int(input('Input N: '))
    X = int(input('Input X: '))
    answer = N % X
    if answer == 0:
        print('I love Python!')
    else:
        print(f"{answer} couples have not availed the discount")

def LoveHistogram():
    n = int(input())
    bars = list(map(int,input().split()))
    char = input()
    for i in range(0, n):
        bar = ""
        for j in range(0,bars[i]):
            bar = bar + char
        print(bar)
        
def Palindrome():
	x = int(input())


    for i in range(x):
		
		a = input().replace(" ", "").lower()
	    b = ""
	
	    for letter in a:
			b = letter + b
	
	
	    if a == b:
			print("Palindrome")
		
	    else:
			print("Not Palindrome")
     
    return

def WhereIsLove():
    inputCoord = input()
    def solve(inputCoord):
        posX = 0 
        posY = 0
        for let in inputCoord:
            if let == "U":           
                posY += 1
            elif let == "D":
            posY -= 1
            elif let == "L":
                posX -= 1
            elif let == "R":
                posX += 1

            if let == "G":
                posX = 0
                posY = 0
            elif let == "V":
                return (posX, posY)
        return(posX, posY)

    x,y = solve(inputCoord)
    print(x, y)
    return

def ValentinesChocolates():
    array = input().split()
    choco = [int(x) for x in array]
    extraChoco = int(input())
    maxChoco = max(choco)
    result = []
    for i in range(len(choco)):
	    if choco[i]+extraChoco >= maxChoco:
		    result.append(True)
	    else:
		    result.append(False)
    result = [str(x) for x in result]
    print(" ".join(result).lower())

def LoveLetters():
    s = input()
    k = 7

    new_s = []
    for character in s:
        if character.isalpha():
            new_character = ord(character) - k
            if character.isupper() and new_character < ord("A"):
                new_character += 26
            elif character.islower() and new_character < ord("a"):
                new_character += 26
            new_s.append(chr(new_character))
        else:
            new_s.append(character)

    print("".join(new_s))

def FLAMES():
    flames = {1: "Friends", 2: "Lovers",
		3: "Affectionate", 4: "Marriage",
		0: "Enemies",} 


    name1 = input().replace(" ", "").lower()

    name2 = input().replace(" ", "").lower()


    for i in name1:
        if i in name2:
            name1 = name1.replace(i, "")
            name2 = name2.replace(i, "")


    length = len(name1) + len(name2)
    print(length, flames[length % 5])
    
    return

def DDayAtValentines():
    successStr = 'mahal na ata kita hehe'
    lockedStr = 'okay ang ako haha'
    key_lock_dict = {
        1: {
            1: True
        },
        2: {
            3: True,
            4: True,
        },
        3: {
            5: True,
            4: True,
        },
        4: {
            3: True,
            5: True,
        },
        5: {
            4: True
        }
    }

    Z = int(input())
    X = int(input())

    if(key_lock_dict.get(Z).get(X)):
        print(key_lock_dict[Z][X])
    else:
        print(lockedStr)






def main():
    choice = int(input("""Please choose a challenge
1.) Line-up Date
2.) Love Histogram
3.) Palindrome
4.) Where is Love?
5.) Valentines Chocolates
6.) Love Letters
7.) Flames
8.) D-Day at Valentines
: """))

    if(choice == 1):
        LineUpDAte()
    elif(choice == 2):
        LoveHistogram()
    elif(choice == 3):
        Palindrome()
    elif(choice == 4):
        WhereIsLove()
    elif(choice == 5):
        ValentinesChocolates()
    elif(choice == 6):
        LoveLetters()
    elif(choice == 7):
        FLAMES()
    elif(choice == 8):
        DDayAtValentines()
main()
