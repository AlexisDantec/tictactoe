m =[[0,1,2,3],
    [1," "," "," "],
    [2," "," "," "],
    [3," "," "," "]]
m_second = m
row = 4
column = 4
count= 0
count_second=0
length_position=0
y=0
x=0
win=0
position= '0,0'
ok=0
win_x=1
win_y=1
winner=' '
count_player_one= 0
count_player_two= 0
count_party = 1
player_one_is_last_winner= 0
player_two_is_last_winner=0
numb_party=0
def print_tab():
    for i in range(0, row):
        for j in range(0, column):
                a = m[i][j]
                print (str(a), end = '|')
        print()
        for j in range(0, column):
            print("_", end = '_')
        print()
#the player choose the position where he would like.he must write the number of the column than a comma than the row.
def where_place():
    global position, length_position, y, x
    position= input('write position : ')
    length_position = len(position)
    y = int(position[0])
    x = int(position[2])


def counter():
    global count
    count+=1

def test_break():
    global ok
    ok =0
    if position[1] !="," or x<1 or x>3 or y<1 or y>3 or length_position != 3:
        print("wrong position")
    else:
        ok=1
#change the caractere on the tab.
def change_box():
    global ok
    test_break()
    if ok==1:
        for i in range (0, row):
            for j in range(0, column):
                if i == x and j == y and m[i][j]==" ":
                    if count % 2 == 0:  
                        m[x][y] = "x"
                    else:
                        m[x][y]= "o"
                    counter()
                elif m[i][j]=="x" and x==i and y==j or m[i][j]=="o" and x==i and y==j:
                    print('wrong position')

def win_row():
    global win_x, win_y, win, winner
    win_x=1
    win_y=1
    while win_x<3:
        while m[win_x][win_y] == m[win_x][win_y +1] and m[win_x][win_y]!=" ":
            if win_y ==2:
                win=1
                winner=m[win_x][win_y]
                return
            win_y+=1
        win_y=1
        win_x+=1

def win_column():
    global win_x, win_y, win, winner
    win_x=1
    win_y=1
    while win_y<3:
        while m[win_x][win_y] == m[win_x+1][win_y] and m[win_x][win_y] != " ":
            if win_x ==2:
                win=1
                winner=m[win_x][win_y]
                return
            win_x+=1
        win_x=1
        win_y+=1

def win_diag():
    global win, winner
    if m[1][1]== m[2][2] and m[2][2]== m[3][3] and m[2][2]!=" " and m[1][1]== m[3][3]:
        win=1
        winner=m[2][2]
    elif m[3][1]== m[2][2] and m[2][2]== m[1][3] and m[2][2]!=" " and m[3][1] == m[1][3]:
        win=1
        winner=m[2][2]

def reset_array():
    for i in range (1, row):
        for j in range(1, column):  
            m[i][j] = " "

player_one=input('Name of the first player :')
player_two=input('Name of the second player :')
numb_party=input('Choose best of how many game you will play ?it must be odd number')
integer_numb_party=int(numb_party)


#set the game number
if integer_numb_party%2==0:
    while integer_numb_party%2==0:
        numb_party= input('it s not a odd number please choose odd number')
        integer_numb_party= int(numb_party)

numb_party_split=int(integer_numb_party/2+1/2)
print(str(numb_party_split))

while count_second< integer_numb_party:
    if count_player_one<numb_party_split and count_player_two<numb_party_split:
        print_tab()
        while count<9 and win !=1:
            if win !=1:
                where_place()
                change_box()
                print_tab()
                if count>3:
                    win_row()
                    win_column()
                    win_diag()
#set who start first next game and set the score

        if winner=="x" and player_one_is_last_winner == 1 and player_two_is_last_winner == 0:
            count_player_two+=1
            player_one_is_last_winner=0
            player_two_is_last_winner=1
        
        elif winner=="o" and player_one_is_last_winner == 1 and player_two_is_last_winner == 0:
            count_player_one+=1
            player_one_is_last_winner=1
            player_two_is_last_winner=0

        elif winner=="x" and player_two_is_last_winner == 1 and player_one_is_last_winner == 0:
            count_player_one+=1
            player_one_is_last_winner=1
            player_two_is_last_winner=0
        
        elif winner=="o" and player_two_is_last_winner == 1 and player_one_is_last_winner == 0:
            count_player_two+=1
            player_one_is_last_winner=0
            player_two_is_last_winner=1
        
        elif winner=="x" and count_player_one == 0 and count_player_two == 0:
            count_player_one+=1
            player_one_is_last_winner=1
            player_two_is_last_winner=0
        
        elif winner=="o" and count_player_one == 0 and count_player_two ==0:
            count_player_two+=1
            player_one_is_last_winner=0
            player_two_is_last_winner=1
        
        if win ==1:
            count_second+=1
            if player_one_is_last_winner==1:
                print(str(player_one)+" win the round with the symbol : " +winner)
            if player_two_is_last_winner==1:
                print(str(player_two)+" win the round with the symbol : " +winner)
        
        elif win==0:
            print('draw')
        print(str(player_one)+ " is at " + str(count_player_one))
        print(str(player_two)+ " is at " + str(count_player_two))
        reset_array()
        count=0
        win=0
        winner=" "
    
    else:
        break

if count_player_one > count_player_two:
     print('the winner is'+player_one)

else:
    print('the winner is'+ player_two)
