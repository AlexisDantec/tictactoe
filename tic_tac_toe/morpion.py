m =[[0,1,2,3],
    [1,"x"," "," "],
    [2," "," "," "],
    [3," "," "," "]]
row = 4
column = 4
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
a = input('write position')
b = len(a)
c = int(a[0])
d =int(a[2])
if a[1] !="," or c<1 or c>3 or d<1 or d>3 or b!= 3:
    print("wrong position")
print(str(c)+ "et" +str(d))
for i in range (0, row):
    for j in range(0, column):
        if i == c and j == d and m[i][j]==" ":
            m[c][d] = "x"
        elif m[i][j]=="x" or m[i][j]=="o":
            print("the box is already used")
print_tab()

