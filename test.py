import time

begin_time = time.clock()


# flatten the list 
def flatten_list(lists):
    results = []
    for numbers in lists:
        results.append(lst)
        return results  



# get the common factors
def common_factors(n):
    myList = []
    for i in range(1, n+1):
        if n % i == 0:
            myList.append(i)

    return myList        


# fucntion to get the answers
def numbers(lsnums, numN, numM):

	for rst in lsnums:
		# return i
	    return common_factors(rst)
	
	# result > numN
	# return result


# numbers(2, 3, 4)





 


first_list = [9, 4, 36, 1]


print "THe numbers are " + str(numbers(first_list, 3, 4))

# should return 3, 3 , 4

print "The program execution time is " + str(time.clock() - begin_time)