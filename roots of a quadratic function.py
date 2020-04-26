import math
a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
dis = b*b-4*a*c

if a != 0:
    if dis > 0:
        root1 = (-b+math.sqrt(dis))/ (2*a)
        root2 = (-b-math.sqrt(dis))/ (2*a)
        print('two roots,''x1 =', root1, 'and x2 =', root2 )

    if dis == 0:
        root = -b / (2*a)
        print('One root: x =', root)

    if dis < 0:
        print("No root")


