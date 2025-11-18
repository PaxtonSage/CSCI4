def m(x, y, o):     #define the function we will use for math
    match o:                  #Switch statement to avoid a bunch of ifs
        case '+':             #if add
            return x+y        #reuturn added number
        case '*':             #if multiply
            return x*y        #return the numbers
        case '-':            #if minus
            return x-y         #return x-y
        case '/':            #if division
            if y!=0:     #check to avoid impossible divison error
                return x/y       #return division
            else:             #else for if the denominator is 0, gotta return something
                return 'no work' # anything divided by 0 is undefined
#TESTS
print(m(5, 20 , '+'))
print(m(15, 2 , '/'))
print(m(1.423, 1.423 , '*'))
print(m(1, 0, '/'))
print(m(2, -2, '-'))
