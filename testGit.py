#This is an OOP adder
import sys
class Adder:
	def __init__(self,origin):
		self.data=origin
	def add(self,x,y):	
		print("Not Implemented")
	def __add__(self,other):
		return Adder(self.data+other)
"""
class ListAdder(Adder):
	def add(self):
		self.sum=self.data[0]+self.data[1]
		return self.sum

class DictAdder(Adder):
	def add(self,dict1,dict2):
		new={}
		key1=list(dict1.keys())
		key2=list(dict2.keys())
		for next in key1:
			val=dict1[next]
			new.update({next:val})
		for next2 in key2:
			val2=dict2[next2]
			new.update({next2:val2})
		return new
"""

if __name__=='__main__':

 	A=Adder(3)
 	B=A+7
 	C=Adder('Dirk')
 	D=C+"Nowitzki"
 	print(B.data)
 	print(D.data)
 	print(f.data)
