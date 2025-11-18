def m(x, y, o):
    match o:
        case '+':
            return x+y
        case '*':
            return x*y
        case '-':
            return x-y
        case '/':
            if y!=0:
                return x/y
            else:
                return 'no work'
        
print(m(5, 20 , '+'))
print(m(15, 2 , '/'))
print(m(1.423, 1.423 , '*'))
print(m(1, 0, '/'))
print(m(2, -2, '-'))