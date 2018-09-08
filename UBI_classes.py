
        
class Consumer:
	def __init__(self, number):
		self.number = number
		self.utility_curves = []  #not sure if need this
		self.utility_param_array = []  #not sure if need this, but think so

		self.demand_curves = []
		self.labor_supply_curve = []
		
		#are goods bought and prices paid something I should be tracking, is this duplicative of seller info
		self.good_bought = []
		self.prices_paid = []
		#maybe its fine, tracking in two places might help adding consistency checks later
		
		self.hours_worked = 0
		self.wages_earned = 0
		self.group_members = 0
		self.fixed_income = 0
		self.total_budget = 0
		

class Seller:
	def __init__(self, number):
		self.number = number
		self.supply_curve = []
		self.labor_demand_curve = []
		self.production_params = []
		self.cost_params = []

		
		self.hours_hired = 0
		self.wages_paid = 0
		self.goods_produced = 0
		self.price = 1
		
		









		
		