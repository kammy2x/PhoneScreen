def setup():
    size(800, 600)
    x = 0
    while x < 800:
        y = 0
        while y < 600:
            if x % 200 == 0:
                fill(41, 128, 185)
            else:
                fill(244, 208, 63)
            rect(x, y, 100, 100)
            y = y + 100
        x = x + 100
   
         
