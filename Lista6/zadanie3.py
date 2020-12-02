def look_and_say(s):
    result = []
    i = 0
    while i < len(s):
        count=1
        while i + 1 < len(s) and s[i] == s[i+1]:
            i+=1
            count +=1
        result.append(str(count) + s[i])
        i+=1
    return ''.join(result)

n = int(input("Wproawdz liczbe wyrazow ciagu look-and-say: "))
s= '1'
print(s)
for i in range(n-1):
    s = look_and_say(s)
    print(s)