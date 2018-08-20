
from UBI_classes import *
#when I have multiple utility functions in future maybe comment out ones I'm not using
from util_Cobb_Douglas import *



#START MAIN

beVerbose = True

num_consumers  = 2
num_sellers = 1

starting_wage = 15

consumer_array = []
seller_array = []


#set names of utility related functions here from modules
Load_Params = Cobb_Douglas_Utility_Load_Params
Utility = Cobb_Douglas_Utility
Build_Demand_Curve = Cobb_Douglas_Build_Demand_Curve



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
	#self.good_bought = []  maybe this needs to wait on seller specification or not?
	#self.prices_paid = [] maybe this needs to wait on seller specification or not?
	#this one sets up demand, maybe also should move
	#setting parrementers ehre but need to move elsewhere
	min_price = 1
	max_price = 200
	price_step = 1
	for j in range(num_sellers + 1):
		consumer_array[i].demand_curves.append(Build_Demand_Curve(min_price, max_price, price_step, 
		                                                        consumer_array[i].budget, 
		                                                        consumer_array[i].utility_param_array[j]))
	#maybe set these later after seller bit?	
	#self.good_bought = []
	#self.prices_paid = []




#now building the total demand curve from the individual demand curves
total_demand = []
for i in range(num_sellers + 1):
	total_demand.append({})
	for price in range(min_price,max_price):
		for j in range(num_consumers):
			total_demand[i][price]=+consumer_array[j].demand_curves[i][price]
		








#creating sellers
for i in range(num_sellers):
	seller_array.append(Seller(i))

### tests

if beVerbose:
	for o in consumer_array:
		print('Consumer #',o.number,vars(o))
	
	for o in seller_array:
		print('Seller #',o.number,vars(o))	
		
	
	
	pass



































