def linear_interpolate(x1, x2, y1, y2, x=0, y=0):
    '''Linearly interpolates to find y or x, depending on which values are entered'''
    if x ==0 and y == 0:
        print('Not enough parameters')
    elif y == 0:
        return ((y2-y1)*(x-x1))/(x2-x1) + y1
    else:
        return ((x2-x1)*(y-y1))/(y2-y1) + x1

print(linear_interpolate(1,5,1,5,x=2))
