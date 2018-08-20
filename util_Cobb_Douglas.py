
from UBI_classes import *



#seed the pseudorandom number generator
#bet there is better way with numpy
#might also be better to do Gaussian variables, consider that later
from random import seed
from random import random
# seed random number generator
seed(1)

def Cobb_Douglas_Utility_Load_Params(num_products):
	total = 0
	param_array = []
	
	#generate a random number for each product including leisure
	for i in range(num_products+1):
		temp = random()
		param_array.append(temp)
		total = total + temp
		
		
	#set the random to sum to 1
	#note could do this with matrix multiplication 
	for i in range(num_products+1):
		param_array[i] = param_array[i] / total

	return param_array
	
def Cobb_Douglas_Utility(param_array, num_products, product_quantities):
	product_total = 1
	 
	for i in range(num_products+1):
		product_total = product_total*(product_quantities[i]^param_array[i])
	return product_total


def Cobb_Douglas_Build_Demand_Curve(min_price, max_price, price_step, income, alpha):
	demand={} #trying this as dictionary
	# could do this with a while look and make step work the way it
	for price in range(min_price,max_price):
		demand[price] = alpha * income / price
	return demand















