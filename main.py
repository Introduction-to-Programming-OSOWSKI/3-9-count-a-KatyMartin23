def countA (w):

    count = 0 

    for i in range (0, len(w)-1):
        if w[i] == "a":
            count = count + 1
    return count

print (countA("dog"))
        
