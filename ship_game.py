from ship_game_bord import bord
import random


def makeShip2():
    global shipIndex1
    global shipIndex2
    shipIndex1 = random.randrange(0, len(bord))
    global shipSign
    shipSign = random.choice(['+', '-', '-10', '+10'])

    ship1 = []
    ship1.append(bord[shipIndex1])

    if shipSign == '+':
        shipIndex2 = shipIndex1 +1
        if len(bord) <shipIndex2 or 0 > shipIndex2:
            ship1.append(bord[shipIndex1 - 1])
            shipSign = '-'
            return ship1
        a = set(bord[shipIndex1])
        b = set(bord[shipIndex2])
        a = list(a)
        b = list(b)
        a.sort()
        b.sort()
        if a[1] in b[1]:
            ship1.append(bord[shipIndex2]) 
        else:
            ship1.append(bord[shipIndex1 - 1])
            shipSign = '-'


    elif shipSign == '-':
        shipIndex2 = shipIndex1 -1
        if len(bord) <shipIndex2 or 0 > shipIndex2:
            ship1.append(bord[shipIndex1 + 1])
            shipSign = '+'
            return ship1
        a = set(bord[shipIndex1])
        b = set(bord[shipIndex2])
        a = list(a)
        b = list(b)
        a.sort()
        b.sort()
        if a[1] in b[1]:
            ship1.append(bord[shipIndex2])
        else:
            ship1.append(bord[shipIndex1 + 1])
            shipSign = '+'
        
    elif shipSign == '-10':
        shipIndex2 = shipIndex1 - 10
        if len(bord) <shipIndex2 or 0 > shipIndex2:
            shipIndex2 = shipIndex1 + 20
            ship1.append(bord[shipIndex2])
            shipSign = '+10'
        else:
            ship1.append(bord[shipIndex2])
        

    elif shipSign == '+10':
        shipIndex2 = shipIndex1 + 10
        if len(bord) < shipIndex2 or 0 > shipIndex2:
            shipIndex2 = shipIndex1 - 20
            ship1.append(bord[shipIndex2])
            shipSign = '-10'
        else:
            ship1.append(bord[shipIndex2])

    return ship1




def makeShip3():
    twoSeaterShip = makeShip2()
    if shipSign == '+' or '-':
        if shipSign == '+':
            shipSign2 = random.choice(['+', '-'])
            if shipSign2 == '+':
                shipIndex3 = shipIndex2 +1
                if len(bord) <shipIndex3 or 0 > shipIndex3:
                    twoSeaterShip.append(bord[shipIndex2 - 2])
                    return twoSeaterShip
                a = set(bord[shipIndex1])
                b = set(bord[shipIndex2])
                c = set(bord[shipIndex3])
                a = list(a)
                b = list(b)
                c = list(c)
                a.sort()
                b.sort()
                c.sort()
                if (b[1] in a[1]) and (b[1] in c[1]):
                    twoSeaterShip.append(bord[shipIndex3]) 
                else:
                    twoSeaterShip.append(bord[shipIndex2 - 2])
            else:
                shipIndex3 = shipIndex1 -1
                if len(bord) <shipIndex3 or 0 > shipIndex3:
                    twoSeaterShip.append(bord[shipIndex2 + 1])
                    return twoSeaterShip
                a = set(bord[shipIndex1])
                b = set(bord[shipIndex2])
                c = set(bord[shipIndex3])
                a = list(a)
                b = list(b)
                c = list(c)
                a.sort()
                b.sort()
                c.sort()
                if (a[1] in b[1]) and (a[1] in c[1]):
                    twoSeaterShip.append(bord[shipIndex3])
                else:
                    twoSeaterShip.append(bord[shipIndex2 + 1])




        elif shipSign == '-':
            shipSign2 = random.choice(['+', '-'])
            if shipSign2 == '+':
                shipIndex3 = shipIndex1 +1
                if len(bord) <shipIndex3 or 0 > shipIndex3:
                    twoSeaterShip.append(bord[shipIndex2 -1])
                    return twoSeaterShip
                a = set(bord[shipIndex1])
                b = set(bord[shipIndex2])
                c = set(bord[shipIndex3])
                a = list(a)
                b = list(b)
                c = list(c)
                a.sort()
                b.sort()
                c.sort()
                if (a[1] in b[1]) and (a[1] in c[1]):
                    twoSeaterShip.append(bord[shipIndex3])
                else:
                    twoSeaterShip.append(bord[shipIndex2 -1])
            else:
                shipIndex3 = shipIndex2 -1
                if len(bord) <shipIndex3 or 0 > shipIndex3:
                    twoSeaterShip.append(bord[shipIndex1 +1])
                    return twoSeaterShip
                a = set(bord[shipIndex1])
                b = set(bord[shipIndex2])
                c = set(bord[shipIndex3])
                a = list(a)
                b = list(b)
                c = list(c)
                a.sort()
                b.sort()
                c.sort()
                if (b[1] in a[1]) and (b[1] in c[1]):
                    twoSeaterShip.append(bord[shipIndex3])
                else:
                    twoSeaterShip.append(bord[shipIndex1 +1])
                    


    
        
        elif shipSign == '+10':
            shipSign2 = random.choice(['+10', '-10'])
            if shipSign2 == '+10':
                shipIndex3 = shipIndex2 + 10
                if len(bord) <shipIndex3 or 0 > shipIndex3:
                    shipIndex3 = shipIndex1 - 10
                    twoSeaterShip.append(bord[shipIndex3])
                else:
                    twoSeaterShip.append(bord[shipIndex3])

            else:
                shipIndex3 = shipIndex1 - 10
                if len(bord) <shipIndex3 or 0 > shipIndex3:
                    shipIndex3 = shipIndex2 + 10
                    twoSeaterShip.append(bord[shipIndex3])
                else:
                    twoSeaterShip.append(bord[shipIndex3])


        elif shipSign == '-10':  
            shipSign2 = random.choice(['+10', '-10'])
            if shipIndex2 == '+10':
                shipIndex3 = shipIndex1 + 10
                if len(bord) < shipIndex3 or 0 > shipIndex3:
                    shipIndex3 = shipIndex2 - 10
                    twoSeaterShip.append(bord[shipIndex3])
                else:
                    twoSeaterShip.append(bord[shipIndex3])

            else:  
                shipIndex3 = shipIndex2 - 10
                if len(bord) < shipIndex3 or 0 > shipIndex3:
                    shipIndex3 = shipIndex1 + 10
                    twoSeaterShip.append(bord[shipIndex3])
                else:
                    twoSeaterShip.append(bord[shipIndex3])
        


    return twoSeaterShip


        
    




    # if twoSeaterShip
    # shipSign = random.choice(['+', '-'])
    

        



if __name__ == '__main__':
    print(makeShip3())













