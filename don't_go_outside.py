series_of_numbers = (1,2,3,4,5,6,7,8,9,10,11)
odd_number = 0
even_number = 0
for i in series_of_numbers:
    if (i%2!=0):
        odd_number+=1
    else:
        even_number+=1
print("count the no of odd numbers from the series is :",odd_number)
print("count the even numbers from the series is :",even_number)