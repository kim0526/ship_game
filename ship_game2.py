import ship_game
import ship_game_bord






def get_ship_index():
    

    global threeSeaterShip
    threeSeaterShip = ship_game.makeShip3()

    global threeSeaterShip2
    threeSeaterShip2 = ship_game.makeShip3()


    global twoSeaterShip
    twoSeaterShip = ship_game.makeShip2()

   

    if threeSeaterShip in twoSeaterShip:
        threeSeaterShip.remove(ship_game.makeShip2)

    
    if threeSeaterShip in threeSeaterShip2:
        threeSeaterShip.remove(ship_game.makeShip2)
 



    if threeSeaterShip2 in threeSeaterShip:
        threeSeaterShip2.remove(ship_game.makeShip2)

    if threeSeaterShip2 in twoSeaterShip:
        threeSeaterShip2.remove(ship_game.makeShip2)
    



    
    


    if twoSeaterShip in threeSeaterShip:
        twoSeaterShip.remove(ship_game.makeShip3)
    if twoSeaterShip in threeSeaterShip2:
        twoSeaterShip.remove(ship_game.makeShip3)


    return threeSeaterShip , twoSeaterShip , threeSeaterShip2






def makebord2():
    i = []
    print_bord_list = []
    print_bord = 10
    print_bord_index = 10
    sum = 1
    count2 = 0
    global hit
    global miss
    miss2 = miss

    # 'OO' 값을 찾기 위해 중첩된 리스트를 순회합니다.
    oo_indices = []
    xx_indices = []


    # for row_index, row in enumerate(ship_game_bord.bord):
    #     for col_index, item in enumerate(row):
    #         if item == 'OO':
    #             oo_indices.append((row_index, col_index))
    # print(oo_indices)
    # oo_indices = [value for value in ship_game_bord.bord if value == 'OO']
    # print(oo_indices.index())

    for index, value in enumerate(ship_game_bord.bord):
        if value == 'OO':
            oo_indices.append(index)

    for index, value in enumerate(ship_game_bord.bord):
        if value == 'XX':
            xx_indices.append(index)
    

    def print_red(text):
        print("\033[91m{}\033[00m".format(text), end=' ')

    def print_blue(text):
        print("\033[94m{}\033[00m".format(text), end=' ')

# 'OO'의 모든 인덱스를 파란색으로 출력하고 10번 마다 줄바꿈을 추가
    for i, item in enumerate(ship_game_bord.bord):
        if i in oo_indices:
            print_blue(item)
        elif i in xx_indices:
            print_red(item)
        else:
            print(item, end=' ')
        if (i+1) % 10 == 0:
            print()

    
    

    

    # oo_indices2 = len(hit)
    # while oo_indices2 > 0:
    #     print(ship_game_bord.bord.index('OO'))
    #     oo_indices2 = oo_indices2 - 1 
    
    
    # while print_bord > 0:

        
        

            
    #     print_bord_index = print_bord_index * sum
    #     sum = sum + 1
    #     print_bord_list = ship_game_bord.bord[:print_bord_index]
        
        
    #     del print_bord_list[:print_bord_index - 10]
    #     print(print_bord_list, sep='\n')
    #     print(" ")
    #     del print_bord_list[:print_bord_index]
    #     print_bord_index = 10
            
    #     print_bord = print_bord - 1





def play():

    
    get_ship_index()
    global attack
    global hit
    global miss
    hit = []
    miss = []
    count = 30
    twoSeaterShip_Ap = 2
    threeSeaterShip_Ap = 3
    threeSeaterShip2_Ap = 3
    
    
    
    print(twoSeaterShip)
    print(threeSeaterShip)
    print(threeSeaterShip2)


    # print(twoSeaterShip)
    # print(threeSeaterShip)
    for i, item in enumerate(ship_game_bord.bord):
        print(item, end=' ')
        if (i+1) % 10 == 0:
            print()
    print()

    while count > 0:
        
        
        
        
        attack = input('어뢰를 발사할 좌표를 입력하세요!! (A ~ J, 0 ~ 99) : ').upper()
        
        
        
        if attack in hit:
            print("이미 타격 성공한 좌표 입니다.")
            continue

        if attack in miss:
            print("이미 타격 실패한 좌표 입니다.")
            continue

        if (attack in twoSeaterShip) or (attack in threeSeaterShip) or (attack in threeSeaterShip2):
            if attack in twoSeaterShip: # 2인승 배에 맞음
                hit.append(attack)
                twoSeaterShip_Ap = twoSeaterShip_Ap - 1
                
                
                 # 목표 좌표의 표시를 바꿈
                
                print("공격이 성공 하였습니다." + attack + " 좌표에 맞았습니다. 남은 기회: {c}".format(c = count))
                print("2인승 전함(1)에 맞았습니다. 침몰까지 남은 공격횟수: {two}".format(two = twoSeaterShip_Ap))
                ship_game_bord.return_index(attack)
                count = count - 1
                if twoSeaterShip_Ap == 0:
                    print("2인승 전함(1)이 침몰하였습니다.")

            elif attack in threeSeaterShip :
                hit.append(attack)
                threeSeaterShip_Ap = threeSeaterShip_Ap - 1 # 3인승 배에 맞음
                count = count - 1
                 # 목표 좌표의 표시를 바꿈
                ship_game_bord.return_index(attack)
                print("공격이 성공 하였습니다." + attack + " 좌표에 맞았습니다. 남은 기회: {c}".format(c = count))
                print("3인승 전함(1)에 맞았습니다. 침몰까지 남은 공격횟수: {three}".format(three = threeSeaterShip_Ap))
                if threeSeaterShip_Ap == 0:
                    print("3인승 전함(1)이 침몰하였습니다.")

            else :
                hit.append(attack)
                threeSeaterShip2_Ap = threeSeaterShip2_Ap - 1 # 3인승 배에 맞음
                count = count - 1
                 # 목표 좌표의 표시를 바꿈
                ship_game_bord.return_index(attack)
                print("공격이 성공 하였습니다." + attack + " 좌표에 맞았습니다. 남은 기회: {c}".format(c = count))
                print("3인승 전함(2)에 맞았습니다. 침몰까지 남은 공격횟수: {three}".format(three = threeSeaterShip2_Ap))
                if threeSeaterShip2_Ap == 0:
                    print("3인승 전함(2)가 침몰하였습니다.")

            

            
                
                


        else:
            count = count - 1
            miss.append(attack)
            ship_game_bord.return_index2(attack)
            print("공격이 실패 하였습니다..." + attack + " 좌표에 맞았습니다. 남은기회: {c}".format(c = count)) 


        makebord2()

        


        
        if (threeSeaterShip_Ap == 0) and (twoSeaterShip_Ap == 0) and (threeSeaterShip2_Ap == 0):
            print("전투에서 승리하셨습니다.")

            return
        
    print("전투에서 패배하였습니다.")
    print(twoSeaterShip)
    print(threeSeaterShip)
    print(threeSeaterShip2)
    
    


def get_attack():
    global attack
    return attack






        
if __name__ == '__main__':
    play()