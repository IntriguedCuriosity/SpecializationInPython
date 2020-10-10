placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."

d={}

for i in placement:
    if i not in d:
        d[i]=0
    d[i]= d[i] + 1
print(d)

ks=d.keys()
min_value=list(d.keys())[0]
for i in ks:
    if d[i] < d[min_value]:
        min_value=d[i]
print(min_value)

str1='hi how are you'
print(str1[0])