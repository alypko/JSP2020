import re
haslo = input("Wprowadz haslo : ")
# print(haslo)
# print(type(haslo))
if  (
    re.search(r"[a-z]", haslo) and
    re.search(r"\d", haslo) and 
    re.search(r"[$#@]", haslo) and 
    re.search(r"[A-Z]", haslo) and 
    6<=len(haslo)<=16
):
    print("good")
else:
    print("error")
# for x in haslo:
#     if re.match(r"/w", x) and re.match([])