
from UBI_classes import *
#when I have multiple utility functions in future maybe comment out ones I'm not using
from util_Cobb_Douglas import *

#when I have multiple production functions in future maybe comment out ones I'm not using
#from prod_linear import *
#sadly I think linear fundamentally doesn't work. needs to have increasing marginal costs
from prod_ln import *


def goods_market(min_price, max_price, price_step, supply_curve, demand_curve, beVerbose):
	excess_demand = True
	clear_price = 0
	clear_q = 0
	for price in range(min_price,max_price):
		if beVerbose:
			print("Price:",price," Q Demanded:", demand_curve[price]," Q Supplies:", supply_curve[price] )
		if(excess_demand and supply_curve[price] >= demand_curve[price]):
			excess_demand = False
			clear_price = price
			clear_q = demand_curve[price]
	if beVerbose:		
		print("Clear Price:",clear_price," Clear Q Demanded:", clear_q )
	#right now returning float quantity, think if it should be floor
	return clear_price, clear_q
	


#START MAIN

#concept now, first do set up then alternate between good market and lobor market
#for goods market, wage is constant
#for labor market, prices of goods are constant


beVerbose = False

num_consumers  = 1
num_sellers = 3

starting_wage = 20
prevailing_wage = starting_wage

consumer_array = []
seller_array = []


#set names of utility related functions from modules
Load_Params = Cobb_Douglas_Utility_Load_Params
Utility = Cobb_Douglas_Utility
Build_Demand_Curve = Cobb_Douglas_Build_Demand_Curve
Build_Labor_Supply_Curve = Cobb_Douglas_Build_Labor_Supply_Curve

#set goods market parameter
min_price = 1
max_price = 200
price_step = 1

#set names of production functions from modules
Load_Production_Params = Ln_Production_Load_Params
Load_Cost_Params = Ln_Production_Load_Cost_Params
Build_Supply_Curve = Ln_Build_Supply_Curve
Build_Labor_Demand_Curve = Ln_Build_Labor_Demand_Curve

################Consumer set up ######################
#creating consumers
for i in range(num_consumers):
	consumer_array.append(Consumer(i))

#loading consumers with initial values
#I should probably move some / all /most of this into modules, either classes or utility
for i in range(num_consumers):
	consumer_array[i].number = i
	#utility curve if i need them
	consumer_array[i].utility_param_array = Load_Params(num_sellers)
	consumer_array[i].hours_worked = 40-1
	consumer_array[i].wages_earned = consumer_array[i].hours_worked * starting_wage 
	#make this random in the future
	consumer_array[i].fixed_income = 1		
	consumer_array[i].budget = consumer_array[i].fixed_income + consumer_array[i].wages_earned
	#make this random in future, maybe with power law
	consumer_array[i].group_members = 100
	#this one sets up demand, maybe also should move
	#setting parrementers ehre but need to move elsewhere

	for j in range(num_sellers + 1):
		consumer_array[i].demand_curves.append(Build_Demand_Curve(min_price, max_price, price_step, 
		                                                        consumer_array[i].budget, 
		                                                        consumer_array[i].utility_param_array[j]))


#!!!!!I bet the below is something i probably need to do a lot
#!!!!!!!!!!!! so the aggregation is something i should at some point pull out and put into a function maybe? 
# not yet though

#now building the total goods demand curve from the individual demand curves
total_demand = []
for i in range(num_sellers + 1):
	total_demand.append({})
	for price in range(min_price,max_price):
		for j in range(num_consumers):
			total_demand[i][price]=+consumer_array[j].demand_curves[i][price]
		


################Seller set up ######################
#creating sellers
for i in range(num_sellers):
	seller_array.append(Seller(i))


#loading Sellers with initial values
#I should probably move some / all /most of this into modules, either classes or utility
for i in range(num_sellers):
	seller_array[i].number = i
	seller_array[i].production_params = Load_Production_Params()
	seller_array[i].cost_params = Load_Cost_Params()
	
	#this one sets up supply, maybe also should move
	#setting parrementers ehre but need to move elsewhere
	min_price = 1
	max_price = 200
	price_step = 1
	seller_array[i].supply_curve = Build_Supply_Curve(min_price, max_price, price_step, 
	                                                  seller_array[i].cost_params, 
	                                                  seller_array[i].production_params, prevailing_wage)



################Initial good prices ######################
for i in range(num_sellers):
#total sellers not total seller +1 because demand for leisure not done ehre
	temp_p, temp_q = goods_market(min_price, max_price, price_step, seller_array[i].supply_curve, total_demand[i], beVerbose)
	seller_array[i].goods_produced = temp_q
	seller_array[i].price = temp_p

##########setup for goods market done   ##################

##########################################################

##########starting setup for labor market ##################

#do the labor market with prices fixed

#building labor supply curves on consumer side, then aggregate to overall labor supply
min_wage = 1
max_wage = 400
wage_step = 1

#building labor supply curves for each customer segment
for i in range(num_consumers):
	consumer_array[i].labor_supply_curve = Build_Labor_Supply_Curve(min_wage, max_wage, 
	                                                                wage_step, consumer_array[i].fixed_income, 
	                                                                consumer_array[i].utility_param_array[-1])

#now building the total labor supply curve from the individual supply curves
total_labor_supply = {}
for i in range(num_consumers):
	for wage in range(min_wage,max_wage):
		total_labor_supply[wage]=+consumer_array[i].labor_supply_curve[wage]


#building labor demand curves for each seller segment assuming fixed prices
for i in range(num_sellers):
	seller_array[i].labor_demand_curve = Build_Labor_Demand_Curve(min_wage, max_wage, wage_step, 
	                                                              seller_array[i].cost_params, 
	                                                              seller_array[i].production_params, 
	                                                              seller_array[i].price)

#now building the total labor demand curve from the individual labor demand curves
total_labor_demand = {}
for i in range(num_sellers):
	for wage in range(min_wage,max_wage):
		total_labor_demand[wage]=+seller_array[i].labor_demand_curve[wage]

#now calculating wage and hours worked
temp_wage, temp_hours = goods_market(min_wage, max_wage, wage_step, total_labor_supply, total_labor_demand, beVerbose)

prevailing_wage = temp_wage

########## initial wages and hours done   ##################


#may need to go back through this and scale customer groups by number of members
#also question, with multiple sellers do i need to allocate hours to sellers or does it just magically work


#################################################################
########## now doing iteration phase   ##################

iterations = 100


##########      Start Loop   ##################

for iter in range(0,iterations):
	# build new supply curves, wage fixed
	for i in range(num_sellers):
		seller_array[i].supply_curve = Build_Supply_Curve(min_price, max_price, price_step, 
	    	                                              seller_array[i].cost_params, 
	        	                                          seller_array[i].production_params, prevailing_wage)
	
	# build new demand curves, wage fixed
	for i in range(num_consumers):
		for j in range(num_sellers + 1):
			consumer_array[i].demand_curves.append(Build_Demand_Curve(min_price, max_price, price_step, 
		    	                                                    consumer_array[i].budget, 
		        	                                                consumer_array[i].utility_param_array[j]))
	total_demand = []
	for i in range(num_sellers + 1):
		total_demand.append({})
		for price in range(min_price,max_price):
			for j in range(num_consumers):
				total_demand[i][price]=+consumer_array[j].demand_curves[i][price]

	# find prices and quantities, wage fixed
	for i in range(num_sellers): #total sellers not total seller +1 because demand for leisure not done ehre
		temp_p, temp_q = goods_market(min_price, max_price, price_step, seller_array[i].supply_curve, total_demand[i], beVerbose)
		seller_array[i].goods_produced = temp_q
		seller_array[i].price = temp_p
	
	# build new labor demand curves, prices fixed
	for i in range(num_sellers):
		seller_array[i].labor_demand_curve = Build_Labor_Demand_Curve(min_wage, max_wage, wage_step, 
	    	                                                          seller_array[i].cost_params, 
	        	                                                      seller_array[i].production_params, 
	            	                                                  seller_array[i].price)

	total_labor_demand = {}
	for i in range(num_sellers):
		for wage in range(min_wage,max_wage):
			total_labor_demand[wage]=+seller_array[i].labor_demand_curve[wage]
	
	# build new labor supply curves, prices fixed
	total_labor_supply = {}
	for i in range(num_consumers):
		for wage in range(min_wage,max_wage):
			total_labor_supply[wage]=+consumer_array[i].labor_supply_curve[wage]
	
	# find wage and hours, prices fixed
	temp_wage, temp_hours = goods_market(min_wage, max_wage, wage_step, total_labor_supply, total_labor_demand, beVerbose)
	prevailing_wage = temp_wage
	
	# setting up to print results of each iteration
	temp_print_list = []
	temp_print_list.append(str(iter))
	temp_print_list.append(',')	
	temp_print_list.append('Hours')	
	temp_print_list.append(',')	
	temp_print_list.append(str(temp_hours))
	temp_print_list.append(',')	
	temp_print_list.append('Wage')	
	temp_print_list.append(',')	
	temp_print_list.append(str(prevailing_wage))
	temp_print_list.append(',')	
	for i in range(num_sellers): #total sellers not total seller +1 because demand for leisure not done ehre
		temp_print_list.append('Good'+str(i)+',')	
		temp_print_list.append('price'+','+ str(seller_array[i].price)+',')
		temp_print_list.append('quant'+','+ str(seller_array[i].goods_produced)+',')
	print_string = "".join(temp_print_list)
	print(print_string)



##########      End Loop   ##################



### tests

if beVerbose:
	for o in consumer_array:
		print('Consumer #',o.number,vars(o))
	
	for o in seller_array:
		print('Seller #',o.number,vars(o))	
		
	
	
	pass



































