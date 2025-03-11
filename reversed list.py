#Enter the start and end value
start= int(input("enter the start of the list: "))
end= int(input("enter the end of the list: "))
#make a range of numbers from the input data
result=list(range(start,end+1))
#reverse the range of numbers
reversed_numbers= result[::-1]
#print the result
print(reversed_numbers)