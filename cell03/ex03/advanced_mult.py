i = 0
j = 0
while i <= 10:
    result = ""
    while j <= 10:
        result = result + " " +str(i*j)
        j+=1
    j=0
    print(f"Table de {i}:{result}")
    i+=1
