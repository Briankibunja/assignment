#negative and odd numbers
start= 1
end = 100
for i in range(start, end):
    if i % 2==0:
        result= i+1 
        print(result)

start=-100
end=0

for i in range(start,end):
    if i<0:
        print(i)
