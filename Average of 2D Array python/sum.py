def sum1(input):
    count = 0
    my_sum = 0
    for row in input:
        my_sum += sum(row)
        count=count+5
    return my_sum
	
print sum1([[10, 20, 30, 40, 50],[20, 30, 40, 50, 60],[30, 40, 50, 60, 70],[40, 50, 60, 70, 80],[50, 60, 70, 80, 90]])