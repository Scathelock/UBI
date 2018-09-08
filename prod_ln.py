
from UBI_classes import *
import math 
#sadly I think linear fundamentally doesn't work. needs to have increasing marginal costs


#seed the pseudorandom number generator
#bet there is better way with numpy
#might also be better to do Gaussian variables, consider that later
#maybe fixed costs should also be pulled from a power law distribution, think about it
from random import seed
from random import random
# seed random number generator
seed(1)

def Ln_Production_Load_Params():
	#im thinking something simple, objects produced = C * hours of labor
	param_array = []
	temp = random()*4
	param_array.append(temp)
	return param_array
	
	
def Ln_Production_Load_Cost_Params():
	#im thinking simple, cost = a +  b * hours of labor
	#wait a minute shouldn't B just be the prevailing wage
	# cost in total for x units is a + b * x*ln(x)
	#where b is wage per hour / objects produced per hour
	
	param_array = []
	#these constants are figuratively pulled out of my ass at this point
	temp1 = random()*150
	
	param_array.append(temp1)
	#also note production cost params depend on production params
	#but those are actually available here, so I need some dumb way around it
	#i bet the right way to do this involves inheritance, keep that in mind for later refactor
	
	
	#note if i want to add variable costs other than wages its easy to do, just add another parameter
	return param_array	
	

def Ln_Build_Supply_Curve(min_price, max_price, price_step, cost_param_array, prod_param_array, wage):

#thinking scratch paper
#revenue = number sold times price
#cost = fixed + const * x * ln(x)
#at each price produce until cost is greater than price
#marginal cost is derivative

#derivative of fixed + const * x * ln(x) = const(ln(x)+1)
#price = const(ln(x)+1)
#price/const=ln(x)+1
#price/const-1=ln(x)
#e^(price/const-1)=x
#x = exp( price/const-1  )

	const = wage / prod_param_array[0]

	supply={} #trying this as dictionary
	# could do this with a while look and make step work the way it
	for price in range(min_price,max_price):
	
		tempx = math.exp(price / const - 1) 
		supply[price] = math.floor(tempx)
		
	return supply
	
	
	
#build labor demand curve assuming good price is fixed

def Ln_Build_Labor_Demand_Curve(min_wage, max_wage, wage_step, cost_param_array, prod_param_array, price):

	#thinking scratch paper
	#labor demand curve, marginal cost of labor = marginal revenue product
	#marginal revenue product = units produced by 1 hour * price of unit
	#units produced per hour is from production param array, price is fixed

	#marginal cost is cost of units produced with L+1 hours - units produced with L hours
	# cost in total for x units is a + b * x*ln(x)
	#where b is wage per hour / objects produced per hour
	#call objects produced per hour, k  call wage per hour w, call hours worked L
	# total cost (Lhours) = a + w / k * (k*L)*ln (k*L)
	# total cost (Lhours) = a + w*L*ln(k*L)
	# marginal cost = the derivative = w(ln(k*L)+1)
	#https://www.wolframalpha.com/input/?i=derivative+a+%2B+b*x*ln(c*x)
	#marginal revenue = k * p
	# k * p = w(ln(k*L)+1)   // goal express L in terms of w
	#k * p / w = ln(k*L)+1
	#k * p / w -1 = ln(k*L)
	#k * p / w -1 = ln(k)+ln(L)
	#k * p / w -1 - ln(k) = ln(L)
	#e^( k * p / w -1 - ln(k) ) = L



	labor_demand={} #trying this as dictionary
	# could do this with a while look and make step work the way it should
	units_per_hour = prod_param_array[0]
	
	for wage in range(min_wage,max_wage):
		labor_demand[wage] = math.exp(units_per_hour*price/wage -1 - math.log(units_per_hour))
	return labor_demand













