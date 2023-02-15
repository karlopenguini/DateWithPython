def LineUpDAte():
    return
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
    return

def WhereIsLove():
    return

def ValentinesChocolates():
    return

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
