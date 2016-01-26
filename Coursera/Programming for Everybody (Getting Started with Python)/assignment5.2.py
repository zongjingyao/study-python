largest = None
smallest = None
while True:
    num = raw_input("Enter a number: ")
    if num == "done" : break
    try:
        i_num = int(num)
        if largest == None: 
		    largest = i_num
        elif i_num > largest:
            largest = i_num
        
        if smallest == None: 
		    smallest = i_num
        elif i_num < smallest:
            smallest = i_num
		
    except:
	    print "Invalid input"

print "Maximum is", largest
print "Minimum is", smallest