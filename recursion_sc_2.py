from test import testEqual
def removeWhite(s):
    t=''
    for i in range(len(s)):
        if s[i].strip() == "'":
            continue
        t=t+s[i].strip()  
    #print(t) 
    return t

def isPal(s):
    if len(s.strip()) == 0:
        return True
    elif len(s.strip())>0 and (s[0] == s[-1]):
        return True
    else:
        return False
    li = len(s)-1
    print(s[1:li])
    return isPal(s[1:li]) and True 

testEqual(isPal(removeWhite("x")),True)
testEqual(isPal(removeWhite("radar")),True)
testEqual(isPal(removeWhite("hello")),False)
testEqual(isPal(removeWhite("")),True)
testEqual(isPal(removeWhite("hannah")),True)
testEqual(isPal(removeWhite("madam i'm adam")),True)
