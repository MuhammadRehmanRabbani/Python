
# defining the average function
def average(matrix,matrix_size):

    my_sum = 0 # declaring variable to store sum
    count = 0 # declaring variable to count total elements of 2D array
	
    # this for loop is calculating the sum	
    for i in range(0, matrix_size):
        for j in range(0, matrix_size):
            my_sum = my_sum+ int(matrix[i][j])
            count = count+1
    # calculating the average	
    average = my_sum/count
    return average;

# defining the main function
def main():
    matrix = [] #declaring matrix
    ave = 0
    matrix_size=int(input("Enter N for N x N matrix : ")) #prompt
	
    print("Enter {} Elements in Square Matrix:".format(matrix_size)) # prompt
	
    #this for loop is taking elements from user and storing them to 2D array
    for i in range(0, matrix_size):
        row = []
        for j in range(0, matrix_size):
            row.append(input())
        matrix.append(row)
		
    print("You entered:") #prompt
	
    #printing 2D array
    for i in range(0, matrix_size):
        print(" ".join(matrix[i]))

    # calling the average function to find average of matrix elements		
    ave = average(matrix,matrix_size)
    
	# printing average
    print('Average is: ',ave)

if __name__ == "__main__": main()