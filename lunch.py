import sys
class lunch:
	def __init__(self):
		self.customer=Customer()
		self.employee=Employee()
		self.food = None
	
	def order(self,foodName):
		self.customer.placeOrder(foodName,self.employee)
		self.food = foodName
	
	def result(self):
		res=self.customer.printFood()
		print("The food customer received is :%s" %(res))
		if res == self.food:
			print("The order is correct!")
		else:
			print("The customer is eating shit!!!")
			
class Customer:
	def __init__(self):
		self.food = None
	
	def placeOrder(self, foodName, employee):
		self.food = employee.takeOrder(foodName)
	
	def printFood(self):
		return self.food.myfood

class Employee():
	def takeOrder(self,foodName):
		return Food(foodName)
		
class Food:
	def __init__(self,name):
		self.myfood = name		
		
if __name__ == '__main__':
	LunchA = lunch ()
	LunchA.order('pizza')
	LunchA.result()
	LunchB = lunch()
	LunchB.order('Ramen')
	LunchB.result()
	