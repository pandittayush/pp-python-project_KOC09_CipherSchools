'''Given an integer N and a cake which can be cut into pieces, each cut should be a straight line going from the center of the cake to its border. Also, the angle between any two cuts must be a positive integer. Two pieces are equal if their appropriate angles are equal. 
The given cake can be cut in following three ways: 
Cut the cake into N equal pieces.
Cut the cake into N pieces of any size.
Cut the cake into N pieces such that no two of them are equal'''



for _ in range(int(input())):
    n = int(input())
    if 360%n == 0:
        a1 = 'y' 
    else:
        a1 = 'n' 
    if n <=360:
        a2 = 'y'
    else:
        a2 = 'n' 
    if n <= 26:
        a3 = 'y'
    else:
        a3 = 'n' 
    print(a1,a2,a3)