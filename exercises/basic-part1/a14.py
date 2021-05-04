#Get the least common multiple (LCM) of two positive integers

def lcm(x,y):
    if x>y:
        z=x
    else:
        z=y
    
    while(True):
        if ( (z%x == 0) and (z%y==0)) :
            lcm=z
            break
        z+=1
        
    return lcm

a= int(input('enter 1st number:'))
b=int(input('enter 2nd number:'))

print('lcm is:',lcm(a,b))