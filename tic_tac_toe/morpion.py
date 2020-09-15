m =[[0,1,2,3],
    [1," "," "," "],
    [2," "," "," "],
    [3," "," "," "]]
row = 4
column = 4
c = 0
b=0
y=0
x=0
position= '0,0'
def print_tab():
    for i in range(0, row):
        for j in range(0, column):
                a = m[i][j]
                print (str(a), end = '|')
        print()
        for j in range(0, column):
            print("_", end = '_')
        print()
print_tab()
def where_place():
    global position, b, y, x
    position= input('write position : ')
    b = len(position)
    y = int(position[0])
    x = int(position[2])


def counter():
    global c
    c+=1
if position[1] !="," or x<1 or x>3 or y<1 or y>3 or b!= 3:
    print("wrong position")    
def change_box():
    for i in range (0, row):
        for j in range(0, column):
            if i == x and j == y and m[i][j]==" ":
                if c%2 == 0:  
                    m[x][y] = "x"
                else:
                    m[x][y]= "o"
                counter()
            elif m[i][j]=="x" or m[i][j]== "o" and x==i and y==j:
                print('wrong position')

while c<9:
    where_place()
    change_box()
    print_tab()
