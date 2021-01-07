import string 
alph = string.ascii_lowercase
def encrypt(inp, k):
    result=''
    for i in inp:
        if(i in alph):
            result+=chr((ord(i)+ k - 97)%26 + 97)
        else:
            result+=i
    return result


def decrypt(inp, k):
    result=''
    for i in inp:
        if(i in alph):
            result+=chr((ord(i)- k - 97)%26 + 97)
        else:
            result+=i
    return result





