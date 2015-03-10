

class A(object):
	def __init__(self, a, b, c):
		self.a = a
		self.b = B(b)
		self.c = C(c)

	def __str__(self):
		return "A a={}, b={}, c={}".format(self.a, self.b, self.c)

class B(object):
	def __init__(self, b):
		self.b = b

	def __str__(self):
		return "B b = {}".format(self.b)		

class C(object):
	def __init__(self, c):
		self.c = c

	def __str__(self):
		return "C c = {}".format(self.c)

import pickle

a0 = A(0,10,100)
a1 = A(1,11,101)
a2 = A(2,12,102)

print(a0)
print(a1)
print(a2)

with open('a0.pickle', 'wb') as f:
	pickle.dump(a0, f)
with open('a1.pickle', 'wb') as f:
	pickle.dump(a1, f)  
with open('a2.pickle', 'wb') as f:
	pickle.dump(a2, f)  

a0 = None
a1 = None
a2 = None

with open('a0.pickle', 'rb') as f: 
	a0 = pickle.load(f)     
with open('a1.pickle', 'rb') as f: 
	a1 = pickle.load(f) 
with open('a2.pickle', 'rb') as f: 
	a2 = pickle.load(f) 

print(a0)
print(a1)
print(a2)

print(a0.b)
print(a0.c)