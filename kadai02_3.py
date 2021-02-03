from collections import deque

tsoot = ["S","C","D","H"]
tcard = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

card = int(5)
suuzi = []
soot =[]
check = [0,0]


#入力

for k in range(2):
    yaku = "ハイカード"
    for i in range(card):
        s = input().rstrip().split(' ')
        soot.append(int(s[0]))
        suuzi.append(int(s[1]))
    
    
    #手札出力
    for i in range(5):
        print(tsoot[soot[i]],end="")
        s = suuzi[i] - 1
        print(tcard[s],end=" ")
    print("")


    #flashの判定
    folg = True
    flash = False
    j = 1
    while j < card:
        if soot[0] != soot[j]:
            folg = False
        j += 1

    if folg == True:
        flash = True

    #ストレートの判定
    suuzi.sort()
    #print(suuzi)
    straight = True
    j = 0
    while j <card - 1:
        if suuzi[j + 1] - suuzi[j] != 1:
            straight = False
            break
        j += 1

    if suuzi[4] + suuzi[0] == 14:
        straight = True
        
    #フォースリーペアの確認

    if len(set(suuzi)) == 2:
        if suuzi[2] == suuzi[3] and suuzi[2] == suuzi[1]:
            yaku = "フォーカード"
            check[k] = 7
        else:
            yaku = "フルハウス"
            check[k] = 6


    if len(set(suuzi)) == 3:
        if suuzi[0] == suuzi[1] and suuzi[1] == suuzi[2] or suuzi[1] == suuzi[2] and suuzi[2] == suuzi[3] or suuzi[2] == suuzi[3] and suuzi[3] == suuzi[4]:
            yaku = "スリーカード"
            check[k] = 3
        else:
            yaku = "ツーペア"
            check[k] = 2

    if len(set(suuzi)) ==4:
        yaku = "ワンペア"
        check[k] = 1


    if flash == True:
        yaku = "フラッシュ"
        check[k] = 5

    if straight == True:
        yaku = "ストレート"
        check[k] = 4

    #straightflash
    if flash == True and straight == True:
        yaku = "ストレートフラッシュ"
        check[k] = 8

    #ロイヤルflashの判定
    if flash == True and straight == True and suuzi[4] == 13:
        yaku = "ロイヤルフラッシュ"
        check[k] = 9
        
    print(yaku)
    for i in range(5):
        del suuzi[0]
        del soot[0]

if check[0] > check[1]:
    print("プレイヤー1の勝ち")
elif check[0] == check[1]:
    print("引き分け")
else:
    print("プレイヤー2の勝ち")