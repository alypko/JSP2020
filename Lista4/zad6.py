

  
def rgbtohsv(r, g, b): 
  
    r = r / 255.0
    g = g / 255.0
    b = b / 255.0
  
    maks = max(r, g, b)    
    Min = min(r, g, b)    
    delta = maks - Min       
  
    
    if maks == Min:  
        h = 0
      
    
    elif maks == r:  
        h = (60 * ((g - b) / delta) + 360) % 360
  
    
    elif maks == g: 
        h = (60 * ((b - r) / delta) + 120) % 360
  
 
    elif maks == b: 
        h = (60 * ((r - g) / delta) + 240) % 360
  

    if maks == 0: 
        s = 0
    else: 
        s = (delta / maks) * 100
  

    v = maks * 100
    return h, s, v 
  
r = int(input("R: "))
g = int(input("G: "))
b = int(input("B: "))

  
print("HSV: ",rgbtohsv(r,g,b)) 