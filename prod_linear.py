
from UBI_classes import *
#sadly I think linear fundamentally doesn't work. needs to have increasing marginal costs


#seed the pseudorandom number generator
#bet there is better way with numpy
#might also be better to do Gaussian variables, consider that later
#maybe fixed costs should also be pulled from a power law distribution, think about it
from random import seed
from random import random
# seed random number generator
seed(1)

def Linear_Production_Load_Params():
	#im thinking something simple, objects produced = C * hours of labor
	param_array = []
	temp = random()*4
	param_array.append(temp)
	return param_array
	
	
def Linear_Production_Load_Cost_Params():
	#im thinking simple, cost = a +  b * hours of labor
	#wait a minute shouldn't B just be the prevailing wage
	param_array = []
	#these constants are figuratively pulled out of my ass at this point
	temp1 = random()*150
	
	param_array.append(temp1)
	
	#note if i want to add variable costs other than wages its easy to do, just add another parameter
	return param_array	
	

def Linear_Build_Supply_Curve(min_price, max_price, price_step, income, alpha):

#thinking scratch paper
#revenue = number sold times price
#cost = fixed + number sold * variable cost 
#variabel cost per unit = wage / b 

	supply={} #trying this as dictionary
	# could do this with a while look and make step work the way it
	for price in range(min_price,max_price):
		demand[price] = alpha * income / price
	return demand
	
	
	
#need to add demand for labor somehow too	
	
#thinking

#with price of goods fixed, can figure out quantity of labor demanded at
	
	
	
#everything below here is left over form consumer utility, delete it	
def Cobb_Douglas_Utility(param_array, num_products, product_quantities):
	product_total = 1
	 
	for i in range(num_products+1):
		product_total = product_total*(product_quantities[i]^param_array[i])
	return product_total

















