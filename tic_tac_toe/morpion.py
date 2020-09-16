m =[[0,1,2,3],
    [1," "," "," "],
    [2," "," "," "],
    [3," "," "," "]]
row = 4
column = 4
count= 0
length_position=0
y=0
x=0
win=0
position= '0,0'
ok=0
win_x=1
win_y=1

def print_tab():
    for i in range(0, row):
        for j in range(0, column):
                a = m[i][j]
                print (str(a), end = '|')
        print()
        for j in range(0, column):
            print("_", end = '_')
        print()
#the player choose the position where he would like.he must right the number of the column than a comma than the row.
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
        print("wrong position ")
    else:
        ok=1
#change the caractere on the tab.
def change_box():
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
    global win_x, win_y, win
    win_x=1
    win_y=1
    while win_x<3:
        while m[win_x][win_y] == m[win_x][win_y +1]:
            if win_y ==2:
                win=1
                return
            win_y+=1
        win_y=1
        win_x+=1

def win_column():
    global win_x, win_y, win
    win_x=1
    win_y=1
    while win_y<3:
        while m[win_x][win_y] == m[win_x+1][win_y]:
            if win_x ==2:
                win=1
                return
            win_x+=1
        win_x=1
        win_y+=1

def win_diag():
    global win
    if m[1][1]== m[2][2] and m[2][2]== m[3][3] and m[2][2]!=" ":
        win=1
    elif m[3][1]== m[2][2] and m[2][2]== m[1][3] and m[2][2]!=" ":
        win=1

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
        print(win)
if win==0:
    print('draw')
