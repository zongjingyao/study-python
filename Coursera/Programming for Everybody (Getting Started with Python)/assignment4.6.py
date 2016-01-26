def computepay(h,r):
    if(h > 40):
	    pay = 40 * r + (h - 40) * r * 1.5
    else:
	    pay = h * r
    return pay

hrs = raw_input("Enter Hours:")
rate = raw_input("Enter Rate:")
p = computepay(float(hrs), float(rate))
print p