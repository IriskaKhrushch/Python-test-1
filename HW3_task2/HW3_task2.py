n = 5583
print("Input value is: ", n) 
l = list(str(n))
d = 1
for i in l:
    d = d * int(i)
print(d)
l.reverse()
print(l)  
l.sort()
print(l)