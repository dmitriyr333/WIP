''' calculate if rectanble a) overlaps b) touches edges c) is inside one another '''
def calculate_overlap( coor1, dim1, coor2, dim2 ):
    
    # finding FURTHEST starting point from both rectanbles (x or y coordinate)
    furthest_start = max( coor1, coor2)

    # now finding CLOSEST ending point
    closest_end = min( coor1+dim1, coor2+dim2 )

    # they will overlap if __second__ rectangle's line starts before \
    # __first__ rectangle ends
    if furthest_start > closest_end:
        return (None, None)

    # if they overlap, calculate coordinates
    overlap = closest_end - furthest_start 

    return (furthest_start, overlap)

def rectangle( r1, r2 ):

    # use helper function to calculate overlap
    x_over, w_over = calculate_overlap( r1['x'], r1['w'], r2['x'], r2['w'] )
    y_over, h_over = calculate_overlap( r1['y'], r1['h'], r2['y'], r2['h'] )

    if not x_over and not y_over:
        print 'No overlap.'
        return None  
    else:
        return {'x':x_over, 'y':y_over, 'w':w_over, 'h':h_over }

if __name__ == '__main__':
    rec1 = {'x':1, 'y':1, 'w':2, 'h':3}
    # rec2 = {'x':6, 'y':5, 'w':6, 'h':3}
    rec2 = {'x':3, 'y':1, 'w':1, 'h':2}

    print rectangle( rec1, rec2 )
